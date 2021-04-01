import pytest
import allure
import os


@pytest.fixture(scope='function')
def login():
    print("登录")
    yield
    print("登录完成")


@allure.feature('加入购物车')
def test_1(login):
    """将苹果加入购物车"""
    print("测试用例1")


@allure.feature('加入购物车')
def test_2():
    """将橘子加入购物车"""
    print("测试用例2")


if __name__ == "__main__":
    # 执行pytest单元测试，生成 Allure 报告需要的数据存在 /temp 目录
    pytest.main(['--alluredir', './Python_Pytest/temp'])
    # 执行命令 allure generate ./temp -o ./report --clean ，生成测试报告
    os.system('allure generate ./Python_Pytest/temp -o ./report --clean')

"""
执行测试生成Allure报告所需要的测试结果数据。在pytest执行测试的时候，指定–alluredir参数及测试数据保存的目录即可

pytest 测试文件所在路径 --alluredir 生成的测试结果数据保存的目录
3、生成测试报告，将上一步骤中的xml文件转成html报告保存在指定目录下

allure generate 测试结果数据所在目录 -o 测试报告保存的目录 --clean

"""

"""
@allure.feature # 用于描述被测试产品需求
@allure.story # 用于描述feature的用户场景，即测试需求
with allure.step # 用于描述测试步骤，将会输出到报告中
allure.attach # 用于向测试报告中输入一些附加的信息，通常是一些测试数据，截图等
@pytest.allure.step # 用于将一些通用的函数作为测试步骤输出到报告，调用此函数的地方会向报告中输出步骤
"""
