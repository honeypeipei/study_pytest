# @File  : test_dict.py
# @Author: leipei
# @Date  :  2020/06/29

class Testdicts:
    def test1(self):
        a = dict(name = 'Bob', age = 40)
        #拉链式键值对
        # b = dict(zip(['name','age'],['Bob',40]))

        #所有键
        print(a.keys())
        d = list(a.keys())
        print(d)

        #所有键+值
        print(a.items())
        # print(b)