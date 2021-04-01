import pytest


@pytest.mark.run(order=1)
def test_one():
    print('\n1')
    assert 1 == 1


@pytest.mark.run(order=2)
def test_two():
    print('\n2')
    assert 1 == 1


@pytest.mark.run(order=4)
def test_four():
    print('\n4')
    assert 1 == 1


@pytest.mark.run(order=3)
def test_three():
    print('\n3')
    assert 1 == 1


# 冒烟测试
def smoke_test():
    pytest.main(['-k', 'test_', '-v'])


if __name__ == '__main__':
    smoke_test()
