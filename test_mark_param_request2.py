# @File  : test_mark_param_request2.py
# @Author: leipei
# @Date  :  2020/06/29

import pytest

test_user_data = [{"user":"Linda", "password":"888888"},
                  {"user":"Tome", "password":"111111"},
                  {"user":"Jone","password":""}]

@pytest.fixture(scope='module')
def login_r(request):
    #可以通过dict形式，虽然传递一个参数，但通过key的方式可以达到类似传入多个参数的效果
    user = request.param['user']
    pwd = request.param['password']

    print("\n打开首页准备登录，登录用户：%s,密码： %s" % (user, pwd))
    if pwd:
        return True
    else:
        return  False

#这是pytest的参数化数据驱动，indirect=True 是把login_r当作函数去执行
@pytest.mark.parametrize("login_r", test_user_data, indirect=True)
def test_cart(login_r):
    a = login_r
    print("测试用例中login的返回值：%s" % a)
    assert a, "失败原因：密码为空"