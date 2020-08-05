# @File  : characterCount.py
# @Author: leipei
# @Date  :  2020/08/05

# 计算一个字符串中每个字符出现的次数
# message = 'It was a bright cold day in April, and the clocks were striking thirteen'
# count = {}
#
# # 遍历字符串
# for character in message:
#     count.setdefault(character, 0)
#     count[character] += 1
# print(count)

import  pprint
message = 'It was a bright cold day in April, and the clocks were striking thirteen'
count = {}
for c in message:
    count[c] = count.setdefault(c,0)
    count[c] += 1


pprint.pprint(count)#字典中嵌套列表或字典用pprint.pprint(),格式打印，键排序
