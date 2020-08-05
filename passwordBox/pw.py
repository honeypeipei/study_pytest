#! python3
# pw.py - An insecure password locker program.

'''
口令保管箱

将账号密码存到保管箱中
用命令打开管理器，将制定账号的密码拷贝到剪贴板上，
再将它粘贴到网站的密码框中
'''
import sys,pyperclip


PASSWORDS = {'email':'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
             'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
             'luggage': '123456'}


if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1] #first command line arg is the account name


if account in PASSWORDS:
    # 将口令复制到剪贴板
    pyperclip.copy(PASSWORDS[account])

    # 提示，已复制了该值
    print('Password for ' + 'account' + 'copied to clipboard.')
else:
    # 库里没有该值也给出提示
    print('There is no account named' + account)