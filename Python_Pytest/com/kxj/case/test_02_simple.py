"""
分组测试
类前面加上 Test 否则将跳过该类

pytest -k TestClassDemo -q
"""


class TestClassDemo:
    def test_one(self):
        assert 1 == 1

    def test_two(self):
        assert 1 == 0

    def test_three(self):
        assert 1 == 1
