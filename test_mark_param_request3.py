# @File  : test_mark_param_request3.py
# @Author: leipei
# @Date  :  2020/06/29
import pytest

test_user_data1 = [{"user":"Linda", "password":"888888"},
                  {"user":"Tome", "password":"111111"},
                  {"user":"Jone","password":""}]

test_user_data2 = [{"q":"中国平安", "count":3,"page":1},
                   {"q":"阿里巴巴", "count":2,"page":2},
                   {"q":"pdd","count":3,"page":1}]


@pytest.fixture(scope='module')
def login_r(request):
    #可以通过dict形式，虽然传递一个参数，但通过key的方式可以达到类似传入多个参数的效果
    user = request.param['user']
    password = request.param['password']

    print("\n用户名：%s, 密码：%s" % (user, password))


@pytest.fixture(scope="module")
def query_param(request):
    q = request.param['q']
    count = request.param['count']
    page = request.param['page']
    print("查询的搜索词：%s" %q)
    return request.param


#这是pytest的参数化数据驱动，indirect=True 是把login_r当作函数去执行
#从下往上执行
#两个数据进行组合调试有3*3个调试用例执行(test_user_data1的个数*test_user_data2的个数)
@pytest.mark.parametrize("query_param", test_user_data2, indirect=True)
@pytest.mark.parametrize("login_r", test_user_data1, indirect=True)
def test_login(login_r,query_param):
    #登录用例
    print(login_r)
    print(query_param)
