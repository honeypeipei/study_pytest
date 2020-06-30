# @File  : test_fixture.py
# @Author: leipei
# @Date  :  2020/06/29

import pytest

def test_cart(login):
    print("\n用例1，登录后执行添加购物车功能操作")

def test_search():
    print("\n用例2，不需要登录，搜索功能")

def test_pay(login):
    print("\n用例3，登录后执行支付功能")


if __name__ == "__main__":
    pytest.main()