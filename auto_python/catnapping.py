# @File  : catnapping.py
# @Author: leipei
# @Date  :  2020/08/05

# print('''Dear Alice,
# Eve's cat has been arrested for catnapping, cat burglary, and extortion.
#
# Sincerely,
# Bob''')

# while True:
#     print('Enter your age:')
#     age = input()
#     # 字符串中只包含数字字符非空
#     if age.isdecimal():
#         break
#     print('Please enter a number for your age.')
#
# while True:
#     print('Select a new password (letters and numers only):')
#     password = input()
#
#     # 字符串中包含字母和数字，非空
#     if password.isalnum():
#         break
#     print('Passwords can only have letters and numbers')



def printPicnic(itemsDict, lefWidth, rightWidth):
    print('PICNIC ITEMS'.center(lefWidth + rightWidth, '-'))
    for k,v in itemsDict.items():
        print(k.ljust(lefWidth,'.') + str(v).rjust(rightWidth))

picnicItems = {'sandwiches': 4, 'apples':12, 'cups':4, 'cookies':8000}
printPicnic(picnicItems, 12, 5)
printPicnic(picnicItems, 20, 6)