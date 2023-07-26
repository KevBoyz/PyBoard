from pyboard import *


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


def test_6():
    """
    Implemented:
    -Align Columns in print
    """
    data = [
        Line(['Xp0--', 3332, 132]),
        Line(['life-', 72, 13]),
        Line([6, 1000, 2]),
        Line([333, 2, 400]),
        Line([4, 8, 9]),
    ]
    b = Board(data=data)
    # print(b.standard_impress())
    print(b)


def test_7():
    """
    Implemented:
    -Board validation is now a property
    -pseudo private atributes turned into public
    """
    data = [
        [1, 2, 3],
        [1, 2, 3, 4]
    ]
    b = Board(data=data)
    print(b)


def test_8():
    """
    Implemented:
    -Board is now iterable
    """
    b = Board(3, 3)
    b.numerate()
    for line in b:
        for obj in line:
            print(obj)


def test_9():
    """
    Board
    Implemented:
    -Columns attr now updates
    -Column object discarded, turned into a list
    -Is now possible iterate over board
    -Append method implemented
    Bug Fix:
    -Aligned impress TypeError

    Line
    Implemented:
    -Size limited. Append don't work when the value reaches the max.
    -__get_item__ doesn't raise exceptions.
    """
    b = Board(3, 3)
    b.numerate()
    b.append(Line(data=[9, 9, 9]))
    print(b)


def test_10():
    """
    Board
    Changed:
    -Update is now do by a method.
    -Board setter now check all elements.
    -Method order organized.
    Implemented:
    - __len__()

    Line
    Changed:
    -Length limit was changed by open/close system.
    """
    b = Board(3, 3)
    b.numerate()
    print(b.get_dims())
    b.append(Line(data=[9, 9, 9]))
    print(b.get_dims())
    # b[0].append(1)  # Exception: The Line is closed. It can' receive more elements.


    test_10()
