# @File  : test_twofixture.py
# @Author: leipei
# @Date  :  2020/06/29

import pytest

# @pytest.fixture(autouse=True)#autouse
@pytest.fixture()
def login_r(open_browser):
    print("登录")


@pytest.fixture()
def open_browser():
    print("打开浏览器")


def test_soso(open_browser):
    print("case3")

@pytest.mark.usefixtures("login_r")
def test_cart():
    print("case4")


if __name__ == "__main__":
    pytest.main()
