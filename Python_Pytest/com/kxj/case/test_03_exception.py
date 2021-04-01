"""
关于预期异常的断言

"""

import pytest


# 执行用例，如果此断言失败，将看到函数调用的返回值。编写用例时，可以在assert断言后面加上详细信息，如果此断言失败，则消息将简单地显示在回溯中
def test_function():
    assert 1 == 2, '不相等'


# 预期了将会发生除0异常，用例可以正常通过
def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        assert 1 / 0


# excinfo 是一个 ExceptionInfo 实例，它是引发的实际异常的包装。主要特征是 .type ， .value 和 .traceback
def test_recursion_depth():
    with pytest.raises(RuntimeError) as excinfo:
        def f():
            f()

        f()
    assert "maximum recursion" in str(excinfo.value)


def myfunc():
    raise ValueError("Exception 123 raised")


def test_match():
    with pytest.raises(ValueError, match=r".* 123 .*"):
        myfunc()
