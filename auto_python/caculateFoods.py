# @File  : caculateFoods.py
# @Author: leipei
# @Date  :  2020/08/05

# 计算客人带来实物的总和
allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
             'Bob' : {'ham sandwiches': 3, 'apples': 2},
             'Carol': {'cups': 3, 'apples pies': 1}}
# def totalBrought(guests, item):
#     numBrought = 0
#     for k, v in guests.items():
#         numBrought += v.get(item, 0)
#     return numBrought
#
# print('Number of things being brought:')
# print('-Apples ' + str(totalBrought(allGuests,'apples')))
# print('-Cups ' + str(totalBrought(allGuests,'cups')))
# print('-Ham sandwiches ' + str(totalBrought(allGuests,'ham sandwiches')))
# print('-Cakes ' + str(totalBrought(allGuests,'cakes')))
# print('-Apples pies ' + str(totalBrought(allGuests,'apples pies')))


'''
leipei add
'''
# countnum = {}
# for k,v in allGuests.items():
#     for m,n in v.items():
#         # v.get(m)
#         # print(m,n)
#         if m in countnum:
#             countnum[m] += n
#         else:
#             countnum[m] = n
# # print(countnum)
# for q,l in countnum.items():
#     print(q,l)

def totalNum(param):
    countnum = {}
    for k, v in param.items():
        for m, n in v.items():
            if m in countnum:
                countnum[m] += n
            else:
                countnum[m] = n
    for q, l in countnum.items():
        print(q, l)

totalNum(allGuests)


spam = {}
spam.setdefault('color','black')
print(spam)
