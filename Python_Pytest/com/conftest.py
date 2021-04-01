# 存储参数化数据和函数，模块下的用例执行时，会自动读取conftest.py文件中的数据
import os
import pytest
import yaml


# 加载读取配置文件config.yaml

@pytest.fixture(scope="session", autouse=True)
def env(request):
    """
    修改配置即可调用响应的配置文件
    :param request:
    :return:
    """
    print('\n---------------------测试读取不同配置文件-----------------------\n')
    config_path = os.path.join(request.config.rootdir,
                               "com/kxj/config",
                               "prod",
                               "config.yaml")

    with open(config_path) as f:
        env_config = yaml.load(f.read(), Loader=yaml.SafeLoader)
        print(env_config)
        return env_config
