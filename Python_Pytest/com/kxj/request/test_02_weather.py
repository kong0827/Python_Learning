import requests

test_data = {
    "city": "北京",
    "temphigh": None,
    "templow": None,
    "week": None,
    "date": None
}


def test_get_weather():
    """
    调用天气预报接口
    :return:
    """
    url = 'https://jisutqybmf.market.alicloudapi.com/weather/query'
    header = {"Authorization": "APPCODE 36a6d64593884af1971d218d14a23f9d"}
    params = {"city": test_data.get("city")}
    res = requests.get(url, params=params, headers=header)
    print(res.json()['result'])


if __name__ == '__main__':
    test_get_weather()
