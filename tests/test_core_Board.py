from PyBoard import *


def test_1():
    board = Board(3, 3, blank_spaces=True)
    board.numerate()
    board[0] = [5, 5, 5]
    board[2][0] = None
    print(board)


def test_2():
    data = [
        [1, 2, 3],
        [1, 2, 3]
    ]
    board = Board(3, 3, data=data)
    board[0][0] = None
    board[1][2] = None
    board.numerate()
    print(board)


test_2()
