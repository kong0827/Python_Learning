"""
mock方法
"""

from pathlib import Path


def getssh():
    return Path.home()


def test_getssh(monkeypatch):
    def mockreturn():
        return Path("/abc/.ssh")

    # 模拟Path中的home方法替代原有
    monkeypatch.setattr(Path, "home", mockreturn)

    x = getssh()
    assert x == Path("/abc/.ssh")
