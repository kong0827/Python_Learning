import requests


def get_json(url):
    r = requests.get(url)
    # 返回的响应对象用于测试目的
    return r.json()
