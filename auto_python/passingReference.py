# @File  : passingReference.py
# @Author: leipei
# @Date  :  2020/08/03

# def eggs(someParameter):
#     someParameter.append('Hello')
#
# spam = [1,2,3]
# # tuple1 = (1,2,3)
# eggs(spam)
# # eggs(tuple1)
# print(spam)

import copy

# spam = [2,4,6,8,10]
# spam = ['a','b','c','d']
# b = spam[(int('3')*2)/11]
# a = spam[-1]
# b = spam[:2]
# print(b)


# bacon = [3.14, 'cat', 11, 'cat', True]
# a = bacon.index('cat')
# bacon.append(99)
# bacon.remove('cat')
# print(bacon)

# spam = ['apples', 'bananas', 'tofu', 'cats']
# 将列表处理成字符串用“，”隔开

# def mychange(parameter):
#     res = ''
#     for i in range(len(parameter)-1):
#         res += parameter[i] + ', '
#
#     return (res + 'and ' + parameter[len(parameter)-1])
#
# spam = ['apples', 'bananas', 'tofu', 'cats','leipei','qingqing']
# myres = mychange(spam)
# print(myres)




# 打印字符图网格

# myi = []
# for i in range(9):
#     myj = ''
#     for j in range(6):
#         myj += '.'
#     myi.append(list(myj))
#
#     # print(res, end=",")
# print(myi)

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', '0', '0', '.', '.', '.'],
        ['0', '0', '0', '0', '.', '.'],
        ['0', '0', '0', '0', '0', '.'],
        ['.', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '.'],
        ['0', '0', '0', '0', '.', '.'],
        ['.', '0', '0', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

# res = []
#
# for i in range(len(grid)):
#     l = ''
#     for j in range(len(grid[i])):
#         l = l + grid[i][j]
#     res.append(l)
# print(res)
#
# for p in range(6):
#     for k in range(len(res)):
#         if k == (len(res)-1):
#             print(res[k][p])
#         else:
#             print(res[k][p], end = '')





grid2 = [['.', '.', '.', '.', '.', '.'],
        ['.', '0', '0', '.', '.', '.'],
        ['0', '0', '0', '0', '.', '.'],
        ['0', '0', '0', '0', '0', '.'],
        ['.', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '.'],
        ['0', '0', '0', '0', '.', '.'],
        ['.', '0', '0', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

for i in range(len(grid2)):
    pass
# print(len(grid2[i]))
for p in range(len(grid2[i])):
    for k in range(len(grid2)):
        if k == (len(grid2)-1):
            print(grid2[k][p])
        else:
            print(grid2[k][p], end = '')
