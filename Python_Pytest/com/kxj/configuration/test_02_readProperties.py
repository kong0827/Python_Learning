import pdb


class TestEnv:
    def test_env_demo(self, env):
        host = env['host']['api']
        print(f'请求接口为：{host}')
