import logging

import pytest

log = logging.getLogger(__name__)


def test_logger():
    log.info("info级别")
    log.error("error级别")
    log.debug("debug级别")
    log.warning("warning级别")


if __name__ == '__main__':
    pytest.main()
