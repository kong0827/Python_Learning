import os

import pytest
import yaml


# 解析yaml方法
class Read_Data:
    def __init__(self, file_name):
        """
        使用pytest运行在项目的根目录下运行
        :param file_name:
        """
        self.file_path = os.getcwd() + os.sep + file_name

    def return_data(self):
        with open(self.file_path, "r", encoding='utf-8') as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            return data


# yml读取
def test_data():
    list_data = Read_Data("yaml_data.yaml").return_data()  # 返回yaml文件读取数据
    return list_data


# 多个测试用例运行多次
@pytest.mark.parametrize('data', test_data())
def test_search(data):
    print('-------------', data)


# yml读取
def test_data2():
    list_data = Read_Data("yaml_data2.yaml").return_data()  # 返回yaml文件读取数据
    print(list_data.get('user'))
    print(list_data['user'])
