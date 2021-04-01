import pytest


@pytest.fixture
def first_entry():
    print("/n ----------------")
    return "a"


@pytest.fixture
def order(first_entry):
    print("/n +++++++++++++++++")
    return [first_entry]


def test_string(order):
    order.append("b")
    assert order == ["a", "b"]


def test_int(order):
    order.append(2)
    assert order == ["a", 2]
