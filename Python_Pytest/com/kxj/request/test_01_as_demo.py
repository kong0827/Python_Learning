import pytest
import requests

base_url = "http://localhost:9064/after-sales-order"


def test_find():
    """
    查询审单数及关闭数
    :return:
    """
    url = f'{base_url}/handler/verify-close/count'
    res = requests.get(url)
    print('\n', res.json())
    assert res.status_code == 200


if __name__ == '__main__':
    pytest.main()
