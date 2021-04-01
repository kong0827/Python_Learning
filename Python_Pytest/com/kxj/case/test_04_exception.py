"""
关于预警警告的断言
"""
# import pdb
from Python_Pytest.com.kxj.case.test_04_fooCompare import Foo


# 利用上下文相关的比较
def test_set_comparison():
    set1 = set("2021")
    set2 = set("2020")
    # pdb.set_trace()
    assert set2 == set1


def pytest_assertrepr_compare(op, left, right):
    if isinstance(left, Foo) and isinstance(right, Foo) and op == "==":
        return [
            "比较Foo实例是否相等",
            "values:{} != {}".format(left.val, right.val),
        ]
