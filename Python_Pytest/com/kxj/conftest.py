import pytest
import smtplib

"""
conftest 文件名不可修改
"""


@pytest.fixture(scope="module")
# @pytest.fixture(scope="module", autouse=True)
def smtp_connection():
    print("全局配置文件")
    return smtplib.SMTP("smtp.gmail.com", 587, timeout=5)
