# @File  : test_python(1)dict.py
# @Author: leipei
# @Date  :  2020/06/30

import pytest

def test_01():
    # D = {'spam':2, 'ham':1, 'eggs':2}
    # l= len(D)
    # print('\nD的长度为：',l)
    # print('字典D的所有键为：',list(D.keys()))
    # print('字典D的所有值为：', list(D.values()))
    # print('字典D的所有键值对为：', list(D.items()))
    # print('读取字典D中不存在的键,返回默认值：', D.get('apple'))
    # print(D.get('fruit','banana'))
    # print(D)
    #
    # D2 = {'toast':4, 'muffin':5}
    # D.update(D2)
    # print('update后的D为：', D)
    #
    # #pop a dictionary by key
    # print('用pop删除了字典中的值：', D.pop('muffin'))
    # print('pop后字典D为：', D)
    # assert 'ham' in D
    #
    # #pop a list by position
    # L = ['aa', 'bb', 'cc', 'dd']
    # print('删除列表中最后一项：', L.pop())
    # print('删除列表中索引为1的值：', L.pop(1))
    # print('pop后列表L为：', L)

    #电影数据库
    table = {'1975':'Holy Grail',
             '1979':'Life of Brain',
             '1983':'The Meaning of Life'}

    # year = '1983'
    # movie = table[year]
    print('\n')
    for year in table:
        print(year + '\t' + table[year])


if __name__ == "__main__":
    pytest.main()