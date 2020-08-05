# @File  : birthday.py
# @Author: leipei
# @Date  :  2020/08/05

# birthdays = {'Alice':'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}
#
# while True:
#     print('Enter a name: (blank to quit)')
#     name = input()
#     if name =='':
#         break
#
#     if name in birthdays:
#         print(birthdays[name] + 'is the birday of' + name)
#     else:
#         print('I do not have birthday information for' + name)
#         print('What is their birthday?')
#         bday = input()
#         birthdays[name] = bday
#         print('Birthday database updated.')

picnicItems = {'apples':5, 'cups': 2}
print('I am bringing ' + str(picnicItems.get('eggs', 0)) + ' eggs')
