import configparser
import os

"""
配置文件的读取
"""
curpath = os.path.dirname(os.path.realpath((__file__)))
cfgpath = os.path.join(curpath, "../cfg/cfg.ini")
print(cfgpath)

# 创建关联对象
conf = configparser.ConfigParser()

# 读ini文件
conf.read(cfgpath, encoding="utf-8")

selections = conf.sections()
print(selections)

item = conf.items('DB')
print(item)
