import logging
import os

import pytest
import yaml

"""
yaml 配置文件的读取

"""


def readProperties():
    cur_path = os.path.dirname(os.path.realpath((__file__)))
    config_path = os.path.join(cur_path,
                               "../config",
                               "test.yaml")

    with open(config_path) as f:
        env_config = yaml.load(f.read(), Loader=yaml.SafeLoader)
        return env_config


if __name__ == '__main__':
    print(readProperties())
