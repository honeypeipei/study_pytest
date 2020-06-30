# @File  : test_logging.py
# @Author: leipei
# @Date  :  2020/06/18

import pytest
import logging

def test_log():
    #大写为变量
    logging.debug("this is debug")
    logging.info("info")
    logging.warning("warning")
    logging.error("error")
    logging.critical("critical")
    assert 1 == 1