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


# Upside tests will probably don't work.


def test_4():
    """
    Implemented:
    The data argument is now validated, and now, need to be a list of Line's.
    All lines must have the same number of elements.
    """
    """ Working
    board = Board(3, 3)
    print(type(board[0]) is Line)
    print(board) 
    """
    data1 = [  # Falling
        [9, 2, 3],
        [1, 2, 3]
    ]
    data2 = [  # Working
        Line([9, 2, 3]),
        Line([1, 2, 3])
    ]
    data3 = [  # Falling
        Line([9, 2, 3, 7]),
        Line([1, 2, 3])
    ]
    board = Board(data=data2)
    print(board)


def test_5():
    """
    Implemented:
    -Computing columns.
    """
    data = [
        Line([9, 2, 3]),
        Line([1, 7, 1]),
        Line([6, 1, 2]),
        Line([3, 2, 0]),
        Line([4, 8, 9]),
    ]
    b = Board(data=data)
    print(b.columns)


test_5()
