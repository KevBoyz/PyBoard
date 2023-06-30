from PyBoard import *


def test_1():
    """First test. Start up of project."""
    board = Board(3, 3, blank_spaces=True)
    board.numerate()
    print(board)


def test_2():
    """
    Implemented:
    -Board now can be defined with an array
    -Is now possible edit the values (only update)
    """
    data = [
        [1, 2, 3],
        [1, 2, 3]
    ]
    board = Board(3, 3, data=data)
    board[0][0] = None
    board[1][2] = None
    board.numerate()
    print(board)


def test_3():
    """
    Implemented:
    -Board now can build itself or receive an array with data with no problems.
    -New method get dims implemented: If data is passed, it auto gets the dimensions.
    """
    data = [
        [9, 2, 3],
        [1, 2, 3]
    ]
    # board = Board() -> Exception: Board is empty
    board = Board(3, 3)
    board2 = Board(data=data)
    print(board)
    print(board.get_dims(), '\n')
    print(board2)


test_3()
