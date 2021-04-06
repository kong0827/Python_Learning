"""
测试审核接口
"""
from common import http


def test_approve():
    print("审核")
    http.get("http://localhost:9999/after-sales-order/handler/verify-close/count")