from typing import List, Tuple
from .board_components import Line


class Board:
    def __init__(self,
                 n_lines: int = None,
                 n_columns: int = None,
                 data: List[Line] = None,
                 blank_spaces: bool = False):
        """
        param n_lines: number of lines
        param n_columns: number of lines
        param data: to define the board directly
        param blank_spaces: hide the None values in print
        """
        self.n_lines = n_lines
        self.n_columns = n_columns
        self.blank_spaces = blank_spaces
        # Defining board
        if self.n_lines and self.n_columns:
            self._build()  # Automatic
        elif data:  # Manual
            self.board = data
            self.n_lines, self.n_columns = self.get_dims()
        else:
            raise Exception('The board is empty.')
        self.columns = []  # initialize
        self.index = -1  # For iterate

    def _build(self):
        """
         Builds the board when n_columns and
        n_lines are passed.

        This will create List[Line[None]]
        """
        board = []
        for lin in range(0, self.n_lines):
            line = Line()
            for col in range(0, self.n_columns):
                line.append(None)
            line.close()
            board.append(line)
        self.board = board

    def _set_columns(self) -> List[List]:
        """
         Iter over all lines and get the values in the
        same positions to define columns, then return it.

         The columns atribute need to be updated if any
        changes in board occur.
         """
        columns = []
        for c in range(0, self.n_columns):
            column = []
            for lin in self.board:
                column.append(lin[c])
            columns.append(column)
        return columns

    def append(self, obj):
        if type(obj) == Line and len(obj) == len(self.board[0]):
            self.board.append(obj)
            self._update()
        else:
            raise Exception('Invalid value, you must pass a Line with '
                            'the same number of objects than the first '
                            'line of the board.')

    def _update(self):
        """
        Update some attributes when a value of board changes.
        """
        self.columns = self._set_columns()
        self.n_lines, self.n_columns = self.get_dims()

    def numerate(self):
        """
         Numerate all values in the board that are equal
        to None, with the number of column and line.

         This was created to be used after _build, to help
        the user to know the position of each case.
        """
        i = -1
        for line in self.board:
            i += 1
            j = -1
            for item in line:
                j += 1
                if item is None:
                    self.board[i][j] = f'{i}{j}'

    def standard_impress(self) -> str:
        """
         Returns a string for print that
        contains the board graphically.
        """
        impression = ''
        for line in self.board:
            for obj in line:
                if self.blank_spaces and obj is None:
                    impression += '  '
                else:
                    impression += f'{obj} '
            impression += '\n'
        return impression

    def aligned_impress(self) -> str:
        """
         String for print board graphically
        with alignment.

        Default method for print() response.
        """
        impression = ''
        self._update()
        longest_list = self.get_longest_list()
        for n_line, lin in enumerate(self.board):
            for n_item, item in enumerate(lin):
                length = self.get_len(item)
                longer = longest_list[n_item]
                dif = longer - length
                if length < longer:
                    impression += f"{item}{dif * ' '} "
                else:
                    impression += f'{item} '
            impression += '\n'
        return impression

    def get_longest_list(self) -> List[int]:
        """
          Used by aligned_impress to get the
         longest value of each line.

         Return a list with the lengths of
        the longest elements.
        """
        longest_list = []
        for lin in self.columns:
            longest = self.get_longest_len(lin)
            longest_list.append(longest)
        return longest_list

    def get_longest_len(self, lin: int) -> int:
        """
         Get the longest length element of the
        line passed and return it.
        """
        lens = []
        for item in lin:
            lens.append(self.get_len(item))
        return max(lens)

    def get_dims(self) -> Tuple[int, int]:
        """
         Iter over board and get the number
        of lines and columns.

        Return: (rows, columns)
        """
        row_conter = 0
        longer_row = []
        for row in self.board:
            row_conter += 1
            if len(row) > len(longer_row):
                longer_row = row
        column_conter = len(longer_row)
        return row_conter, column_conter

    @property
    def board(self):
        return self._board

    @board.setter
    def board(self, data):
        """
        A valid board aspects:
        * Is a list of Line's
        * All Line's have the same number of objects
        """
        if type(data) is list:
            for c in range(1, len(data)):
                if type(data[c]) is not Line:
                    raise Exception(f'The value in position [{c}] of the list, is not a Line.')
                if len(data[0]) != len(data[c]):
                    raise Exception('All Line\'s must have the same number of objects.')
            self._board = data
            for line in self.board:
                line.close()
        else:
            raise Exception('Invalid value for "data". You must pass a list of Line\'s.')

    @staticmethod
    def get_len(item) -> int:
        """
        Try to get the len of an item, then return it.
        """
        try:
            length = len(item)
        except TypeError:
            try:
                length = len(str(item))
            except Exception as e:
                raise Exception(f'Value {item} can not be read by len()\n', e)
        return length

    def __setitem__(self, key, value):
        self.board[key] = value

    def __getitem__(self, item):
        return self.board[item]

    def __next__(self):
        if self.index == len(self.board) - 1:
            self.index = -1
            raise StopIteration
        self.index += 1
        return self.board[self.index]

    def __iter__(self):
        return self

    def __str__(self):
        return self.aligned_impress()

    def __repr__(self):
        return str(self.board)

    def __len__(self):
        return self.n_columns, self.n_lines
