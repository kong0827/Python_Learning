#!/usr/bin/python3
# coding=utf-8
import configparser
import logging
import os

from common import constant

"""
配置文件的读取
 -dev:  开发
 -test: 测试
 -prod: 生产
 
 修改读取配置文件的文件名（dev, test, prod） 读取不同的文件
"""

cur_path = os.path.split(os.path.realpath(__file__))[0]
configPath = os.path.join(cur_path, "../resources/", constant.profile, "application.ini")
logging.info("读取{}配置文件", configPath)


class ApplicationConfig:
    def __init__(self):
        self.cf = configparser.ConfigParser()
        self.cf.read(configPath, encoding='UTF-8')

    def get_value(self, section, key) -> object:
        return self.cf.get(section, key)

    def get_token(self, name):
        token_id = self.cf.get("BASE", name)
        return token_id

    def set_value(self, section, key, value):
        self.cf.set(section, key, value)
        config = open(configPath, 'w', encoding='UTF-8')
        with config as conf:
            self.cf.write(conf)
        config.close()


if __name__ == "__main__":
    r = ApplicationConfig()
    s = r.get_value("API", "as_url")
    print(s)
