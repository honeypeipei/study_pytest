# @File  : conftest.py
# @Author: leipei
# @Date  :  2020/06/29

import pytest

#测试方法之前执行的方法
@pytest.fixture(scope="session")#范围扩展到所有测试方法执行之前
def login():
    print("\n请输入用户名密码登录conftest")
    # 遇到yield，先执行测试方法，再回头执行yield之后的代码
    yield
    print("\n退出登录")


