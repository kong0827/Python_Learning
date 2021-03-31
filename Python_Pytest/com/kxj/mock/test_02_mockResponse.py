"""
模拟类
monkeypatch.setattr()可以与类结合使用，以模拟从函数而不是值返回的对象。想象一个简单的函数来获取API URL并返回json响应
"""
import requests

from Python_Pytest.com.kxj.mock.test_02_monketpatching import get_json


class MockResponse:
    """
    定义一个mock类和方法，返回固定json对象
    模拟r需要一个.json()返回字典的方法。可以通过定义一个class来表示在我们的测试文件中r。
    """
    @staticmethod
    def json():
        return {"mock_key": "mock_response"}


def test_get_json(monkeypatch):
    def mock_get(*args, **Kwargs):
        return MockResponse()

    ''' 
    定义一个mock_get方法，无论传入什么参数，都返回上面的mock类，然后使用
    monkeypatch.setattr对requests.get重新设置，这样requests.get有了属性 
    “mock_get”，再次使用时就直接使用了mock_get方法
    '''
    monkeypatch.setattr(requests, "get", mock_get)
    result = get_json("https://fakeurl")
    assert result["mock_key"] == "mock_response"
