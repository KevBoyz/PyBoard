# Getting started

In this tutorial, you'll learn the basic of how crate and manage a Board. (v1.0)

## Defining
The Board can be instantiated by two forms. The first is passing
the number of **lines** and **columns** that you want.
```python
b = Board(2,3)
```
This will generate a board with None value squares.
```python
$ print(board)
None None None
None None None
```
The other form is directly defining the board, passing the **data** atribute.
```python
data = [
    Line([1, 2, 3]),
    Line([4, 5, 6])
]
b = Board(data=data)

$ print(b)
1 2 3
4 5 6
```
The **data** need to be a **list of Line's** and all Line's must have the **same**
number of objects.   
The Line can receive all types of values, but if they can't
be readied by _len()_, some features of Board will don't work.

## Editing and Printing
```python
b = Board(2, 2)

b[0] = Line([11, 12]) # Line
b[1][0] = 9         # Case
b.append(Line([3, 3]) 

$ print(b)
11 12   
9  None 
3  3
```
Once crated, the board defines the number of elements per line, and don't allow
that any row have other length. Because of this, it's not possible do append 
or delete in lines, so make sure init board with the exactly dimensions you need.

To append a new line to board, make sure that you are passing a Line that contains 
the same length of the others.

- The reason why the lines must be the same size is to avoid unevenness and to
ensure that the print is done correctly.

The default print is aligned like this:
```python
1000 34   word
5    2345 123
```
You can also use standard_impress to print without align.
```python
$ print(b.standard_impress())
1000 34 word
5 2345 123
```

## Numerated Board
To edit a board created by automatic build, is recommended that you numerate the
board, in order to facilitate find the squares you want. 
```python
b = Board(2, 2)
b.numerate()

$ print(b)
11 12 
21 22
```

## Iterating over board
Line don't trow exception when you search for an index that don't exist. This is 
util in a project like Minesweeper, because you must check the squares around a square,
and sometimes, the square that you are seen it's on the corner, and an exception is trowed.

On the contrary, the behavior is to return None, in case the value does not exist.