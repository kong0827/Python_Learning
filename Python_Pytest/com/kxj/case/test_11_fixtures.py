import pytest


@pytest.fixture(scope='module', autouse=True)
def test1():
    print('\n开始执行module')
    yield
    print('\n结束module')


@pytest.fixture(scope='class', autouse=True)
def test2():
    print('\n开始执行class')
    yield
    print('\n结束class')


@pytest.fixture(scope='function', autouse=True)
def test3():
    print('\n开始执行function')
    yield
    print('\n结束function')


def test_a():
    print('\n---用例a执行---')


def test_d():
    print('\n---用例d执行---')


class TestCase:

    def test_b(self):
        print('\n---用例b执行---')

    def test_c(self):
        print('\n---用例c执行---')


if __name__ == '__main__':
    pytest.main(['-s', 'pytest_test.py'])
