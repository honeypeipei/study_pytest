# @File  : test_divide.py
# @Author: leipei
# @Date  :  2020/06/18

from  src.caculate import *

class TestDivide():#go to自动生成类名
    def test_divide(self):
        assert divide(10,5) == 2
        # divide(10,0)