# @File  : ticTacToe.py
# @Author: leipei
# @Date  :  2020/08/05


'''
井字键盘
'''
# theBoard = {'top-L':'O', 'top-M':'O', 'top-R':'O',
#             'mid-L':'X', 'mid-M':'X', 'mid-R':'',
#             'low-L':' ', 'low-M':' ', 'low-R':'X'}
# def printBoard(board):
#     print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
#     print('-+-+-')
#     print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
#     print('-+-+-')
#     print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
#
# printBoard(theBoard)




#允许输入
theBoard = {'top-L':' ', 'top-M':' ', 'top-R':' ',
            'mid-L':' ', 'mid-M':' ', 'mid-R':' ',
            'low-L':' ', 'low-M':' ', 'low-R':' '}
def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

# X代表玩家A，O代表玩家B
# 玩家输入字典的键，代表位置
turn = 'X'
for i in range(9):
    printBoard(theBoard)
    print('Turn for ' + turn + '. Move on which space?')
    move = input()
    theBoard[move] = turn

    # turn为当前玩家，轮流输入自己的位置
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'

printBoard(theBoard)