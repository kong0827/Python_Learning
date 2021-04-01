"""
数据驱动
将测试数据准备好，执行的时候自动去读取数据，根据数据的多少执行。数据有10条，那就执行10次，数据有20条，那就执行20次。
"""
import pytest


@pytest.mark.parametrize("x, y", [(1, 2), (2, 2), (3, 3), (4, 4)])
def test_data(x, y):
    print(f'x={x}, y={y}')


# 设置测试数据
testdata = [
    ('', '1', 'ask', '1'),  # token值为空
    ('32de7ca8-09b4-462e-b7b1-c25ed119eac1', '', 'ask', '2'),  # 标题为空
    ('32de7ca8-09b4-462e-b7b1-c25ed119eac1', '1234567890', '', '2'),  # 版块为空
    ('32de7ca8-09b4-462e-b7b1-c25ed119eac1', '1234567890', 'ask', ''),  # 内容为空
]


@pytest.mark.parametrize('token, title, tab, content', testdata)
def test_topic(token, title, tab, content):
    print(f'token={token}, title={title},{tab}={tab}, content={content}')
