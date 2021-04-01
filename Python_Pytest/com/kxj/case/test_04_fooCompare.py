import pytest


class Foo:
    def __init__(self, val):
        self.val = val

    def __eq__(self, other):
        return self.val == other.val


def test_compare():
    f1 = Foo(1)
    f2 = Foo(2)
    assert f1 == f2


if __name__ == '__main__':
    pytest.main(['-q', 'test_04_fooCompare.py'])
