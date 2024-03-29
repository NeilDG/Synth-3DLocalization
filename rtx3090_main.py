import os
import multiprocessing
import time


def train_depth():
    # os.system("python \"train_main.py\" --server_config=3 --img_to_load=-1 "
    #           "--plot_enabled=0 --save_every_iter=500 --network_version=\"depth_v01.18\" "
    #           "--iteration=1")

    # FOR TESTING
    # os.system("python \"train_main.py\" --server_config=3 --img_to_load=-1 "
    #           "--plot_enabled=1 --save_every_iter=500 --network_version=\"depth_v01.17\" "
    #           "--iteration=1")

    os.system("python \"train_main-iid.py\" --server_config=3 --img_to_load=-1 "
              "--plot_enabled=1 --save_every_iter=50 --network_version=\"depth_v01.07_iid\" "
              "--iteration=7")

def test_depth():
    os.system("python \"test_main-iid.py\" --server_config=3 --img_to_load=1000 --plot_enabled=1 --network_version=\"depth_v01.06_iid\" "
              "--iteration=1")

    os.system("python \"test_main-iid.py\" --server_config=3 --img_to_load=1000 --plot_enabled=1 --network_version=\"depth_v01.06_iid\" "
              "--iteration=5")

def train_img2img():
    os.system("python \"train_img2img_main.py\" --server_config=3 --img_to_load=-1 "
              "--plot_enabled=0 --save_every_iter=500 --network_version=\"synth2real_v02.00\" "
              "--iteration=1")
    #
    # os.system("python \"train_img2img_main.py\" --server_config=3 --img_to_load=-1 "
    #           "--plot_enabled=0 --save_every_iter=500 --network_version=\"synth2real_v02.01\" "
    #           "--iteration=1")


def test_img2img():
    os.system("python \"test_img2img_main.py\" --server_config=3 --img_to_load=1000 "
              "--plot_enabled=1 --network_version=\"synth2real_v02.00\" "
              "--iteration=1")

def main():
    # train_depth()
    test_depth()
    #
    # train_img2img()
    #  test_img2img()
    # os.system("shutdown /s /t 1")

if __name__ == "__main__":
    main()