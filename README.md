# pyboard: CLI for boards



## What is it?
A Python package that provides a textual interface
to create board based applications.

Note: Some features are not implemented because this project still in beta.

## Features
* Easy board build and edit.
* An iterable that not trow _out range_ exception (ideal for apps like Minesweeper).
* Save the state of the board in a json file.
* Multiple resources to print to Board, including labels, alignment and blank spaces.
* A way to access lines and columns individually
* Invert X,Y axis (ideal for lan Chess apps)

## Example
```python
board = Board(3,3)
board.numerate()
print(board)
>>> 00 01 02 
    10 11 12 
    20 21 22 

board[1][1] = 555
board[0][0] = 9999
print(board)
>>> 9999 01  02 
     10  555 12 
     20  22  22 
```

## Getting it
`pip install pyboard`

## Technologies used
Python 3.10 pure
