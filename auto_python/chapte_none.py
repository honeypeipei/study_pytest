# @File  : chapte_none.py
# @Author: leipei
# @Date  :  2020/07/28

# spam = print('......')
# print(None == spam)

# print(None == print('hello'))

# a = print()
# print(a)

# print('Hello', end = ' ')
# print('world')

# def spam():
#     eggs = 'spam local'
#     print('这是spam函数中的变量名：'+ eggs)
# def bacon():
#     eggs = 'bacon local'
#     print('这是bacon函数中的变量名'+ eggs)
#     spam()
#     print('这也是bacon函数中的变量'+ eggs)
#
# eggs = 'global'
# bacon()
# print('这是全局变量' + eggs)

#在函数内修改局部变量
# def spam():
# #     global eggs
# #     eggs = 'spam'
# # eggs = 'global'
# # spam()
# # print(eggs)


# def spam(divideBy):
#     try:
#         return 42/divideBy
#     except ZeroDivisionError:
#         print('Error: Invalid argument.')
#
# print(spam(2))
# print(spam(3))
# print(spam(0))
# print(spam(12))


def spam(divideBy):
    return 42 / divideBy

try:
    print(spam(2))
    print(spam(3))
    print(spam(0))
    print(spam(12))
except ZeroDivisionError:
    print('1111111')