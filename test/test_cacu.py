# @File  : test_cacu.py
# @Author: leipei
# @Date  :  2020/06/18

from  src.caculate import *

class TestCase():
    def setup_method(self):
        print('在每个测试方法前执行')
        self.a = 1
        self.b = 2
        self.exp = 3

    def test_add(self):
        assert add(self.a, self.b) == self.exp