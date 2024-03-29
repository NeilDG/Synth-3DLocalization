import os
import multiprocessing
import time


def train_depth():
    # os.system("python3 \"train_main-iid.py\" --server_config=4 --img_to_load=-1 "
    #           "--plot_enabled=0 --save_every_iter=500 --network_version=\"depth_v01.03_iid\" "
    #           "--iteration=1")

    os.system("python3 \"train_main-iid.py\" --server_config=4 --img_to_load=-1 "
              "--plot_enabled=0 --save_every_iter=500 --network_version=\"depth_v01.07_iid\" "
              "--iteration=1")

    os.system("python3 \"train_main-iid.py\" --server_config=4 --img_to_load=-1 "
              "--plot_enabled=0 --save_every_iter=500 --network_version=\"depth_v01.07_iid\" "
              "--iteration=5")

    os.system("python3 \"train_main-iid.py\" --server_config=4 --img_to_load=-1 "
              "--plot_enabled=0 --save_every_iter=500 --network_version=\"depth_v01.07_iid\" "
              "--iteration=7")

def test_depth():
    os.system("python3 \"test_main.py\" --server_config=4 --img_to_load=-1 --plot_enabled=1 --network_version=\"depth_v01.03\" "
              "--iteration=1")

def train_img2img():
    os.system("python3 \"train_img2img_main.py\" --server_config=4 --img_to_load=-1 "
              "--plot_enabled=0 --save_every_iter=200 --network_version=\"synth2real_v01.02\" "
              "--iteration=1")

    os.system("python3 \"train_img2img_main.py\" --server_config=4 --img_to_load=-1 "
              "--plot_enabled=0 --save_every_iter=200 --network_version=\"synth2real_v01.02\" "
              "--iteration=2")

def test_img2img():
    os.system("python \"test_img2img_main.py\" --server_config=4 --img_to_load=1000 "
              "--plot_enabled=1 --network_version=\"synth2real_v01.00\" "
              "--iteration=1")

def main():
    train_depth()
    # test_depth()
    # train_img2img()
    # os.system("shutdown /s /t 1")

if __name__ == "__main__":
    main()