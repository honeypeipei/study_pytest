# @File  : collatz.py
# @Author: leipei
# @Date  :  2020/08/01

def collatz(param):
    if param % 2 == 0:
        res = param //2
        return res
    else:
        res = param * 3 + 1
        return res


while True:
    print('Please input:')
    # 检测用户是否输入了一个非整数的字符串
    try:
        myinput = int(input())
        myres = collatz(myinput)
        if myres != 1:
            print('error,please input agein ')
            continue
        else:
            print('cogratulation! your result is ：', myres)
            break
    except:
        print('Please input a int!!!!!!')
        # myinput = int(input())





