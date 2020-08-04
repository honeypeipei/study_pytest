# @File  : magic8Ball2.py
# @Author: leipei
# @Date  :  2020/08/03
import  random
messages = ['It is certain',
            'Yes definitely',
            'Reply hazy try again',
            'Ask again later',
            'Concentrate and ask again',
            'My reply is no',
            'Outlook not so good',
            'Very doubtful']
print(messages[random.randint(0, len(messages) - 1)])
# 有效的换行符
print('hello '+\
      'leipei...')