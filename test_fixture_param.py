# @File  : test_fixture_param.py
# @Author: leipei
# @Date  :  2020/06/29

import pytest

@pytest.fixture(params=[1,2,3,'Linda'])
def prepare_data(request):
    return request.param

#每个数据驱动测试方法
def test_one(prepare_data):
    print('testdata:%s' % prepare_data)


def test_two(prepare_data):
    if type(prepare_data) is str:
        print('testdata2:%s' % prepare_data)