# Tic Tac Toe

import random

def drawBoard(board):
    # This function prints the board it is passed
    print('    |    |')
    print('  ' + board[7] + ' | ' + board[8] + '  | ' + board[9])
    print('    |    |')
    print('--------------')
    print('    |    |')
    print('  ' + board[4] + ' | ' + board[5] + '  | ' + board[6])
    print('    |    |')
    print('--------------')
    print('    |    |')
    print('  ' + board[1] + ' | ' + board[2] + '  | ' + board[3])


#theBoard = ['O'] *10
letters = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
theBoard = []
random.shuffle(letters)
for i in range(10):
    theBoard.append(letters.pop())

drawBoard(theBoard)
