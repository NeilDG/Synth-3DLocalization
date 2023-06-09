import kornia.metrics.psnr

from config import network_config
from config.network_config import ConfigHolder
import global_config
import torch
from utils import plot_utils, tensor_utils
import lpips
import torch.nn as nn
import numpy as np
from trainers import img2imgtrainer
from testers import depth_metrics

class Img2ImgTester():
    def __init__(self, gpu_device):
        self.gpu_device = gpu_device
        self.img2img_t = img2imgtrainer.Img2ImgTrainer(self.gpu_device)
        self.lpips_loss = lpips.LPIPS(net='vgg').to(self.gpu_device)
        self.l1_loss = nn.L1Loss(reduction='mean')
        self.mse_loss = nn.MSELoss(reduction='mean')

        self.visdom_reporter = plot_utils.VisdomReporter.getInstance()

        self.l1_results = []
        self.mse_results = []
        self.rmse_results = []
        self.psnr_results = []

    #measures the performance of a given batch and stores it
    def measure_and_store(self, input_map):
        use_tanh = ConfigHolder.getInstance().get_network_attribute("use_tanh", False)
        img_a2b, img_b2a = self.img2img_t.test(input_map) #a2b --> real2synth, b2a --> synth2real

        target = input_map["img_a"]

        if(use_tanh):
            img_b2a = tensor_utils.normalize_to_01(img_b2a)
            target = tensor_utils.normalize_to_01(target)

        psnr_result = kornia.metrics.psnr(img_b2a, target, torch.max(target).item())
        self.psnr_results.append(psnr_result.item())

        l1_result = self.l1_loss(img_b2a, target).cpu()
        self.l1_results.append(l1_result)

        mse_result = self.mse_loss(img_b2a, target).cpu()
        self.mse_results.append(mse_result)

        rmse_result = depth_metrics.torch_rmse(img_b2a, target).item()
        self.rmse_results.append(rmse_result)

    def visualize_results(self, input_map, dataset_title):
        version_name = network_config.ConfigHolder.getInstance().get_version_name()
        self.img2img_t.visdom_visualize(input_map, "Test - " + version_name + " " + dataset_title)

    def report_metrics(self, dataset_title):
        version_name = network_config.ConfigHolder.getInstance().get_version_name()

        psnr_mean = np.round(np.mean(self.psnr_results), 4)
        self.psnr_results.clear()

        l1_mean = np.round(np.float32(np.mean(self.l1_results)), 4) #ISSUE: ROUND to 4 sometimes cause inf
        self.l1_results.clear()

        mse_mean = np.round(np.mean(self.mse_results), 4)
        self.mse_results.clear()

        rmse_mean = np.round(np.mean(self.rmse_results), 4)
        self.rmse_results.clear()

        last_epoch = global_config.general_config["current_epoch"]
        self.visdom_reporter.plot_text(dataset_title + " Results - " + version_name + " Last epoch: " + str(last_epoch) + "<br>"
                                       + "PSNR: " +str(psnr_mean) + "<br>" 
                                       "Abs Rel: " + str(l1_mean) + "<br>"
                                        "Sqr Rel: " + str(mse_mean) + "<br>"
                                       "RMSE: " + str(rmse_mean) + "<br>")
