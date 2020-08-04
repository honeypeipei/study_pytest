# @File  : allMyCats.py
# @Author: leipei
# @Date  :  2020/08/03

# print('Enter the name of cat 1 :')
# catName1 = input()
# print('Enter the name of cat 2 :')
# catName2 = input()
# print('Enter the name of cat 3 :')
# catName3 = input()
# print('Enter the name of cat 4 :')
# catName4 = input()
# print('Enter the name of cat 5 :')
# catName5 = input()
# print('Enter the name of cat 6 :')
# catName6 = input()
# print('The cat name are: ')
# print(catName1 + ' ' + catName2 + ' ' + catName3 + ' ' + catName4 + ' ' + catName5 + ' ' + catName6)

#range(len(someList))

supplies = ['pens', 'staplers', 'flame-throwers', 'binders']
for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supplies is: ' + supplies[i])#str(i)将整数强制转换为字符串
