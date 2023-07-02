from typing import List
from .board_components import Line, Column


class Board:
    def __init__(self,
                 n_lines: int = None,
                 n_columns: int = None,
                 data: List[Line] = None,
                 blank_spaces: bool = False):
        self._n_lines = n_lines
        self._n_columns = n_columns
        self.blank_spaces = blank_spaces
        # Defining _board.
        self._board = None
        if self._n_lines and self._n_columns:
            self._build()  # Automatic
        elif data:  # Manual
            if self._validate_data(data):
                self._board = data
                self._n_lines, self._n_columns = self.get_dims()

        else:
            raise Exception('The board is empty.')
        self.columns = self._set_columns()

    def _build(self):
        board = []
        for lin in range(0, self._n_lines):
            line = Line()
            for col in range(0, self._n_columns):
                line.append(None)
            board.append(line)
        self._board = board

    def _impress(self):
        impression = ''
        for line in self._board:
            for obj in line:
                if self.blank_spaces and obj is None:
                    impression += '  '
                else:
                    impression += f'{obj} '
            impression += '\n'
        return impression

    def _set_columns(self):
        columns = []
        for c in range(0, self._n_columns):
            column = Column()
            for lin in self._board:
                column.append(lin[c])
            columns.append(column)
        return columns

    def numerate(self):
        i = -1
        for line in self._board:
            i += 1
            j = -1
            for item in line:
                j += 1
                if item is None:
                    self._board[i][j] = f'{i}{j}'

    def get_dims(self) -> tuple:
        row_conter = 0
        longer_row = []
        for row in self._board:
            row_conter += 1
            if len(row) > len(longer_row):
                longer_row = row
        column_conter = len(longer_row)
        return row_conter, column_conter

    @staticmethod
    def _validate_data(data):
        if type(data) is list and type(data[0]) is Line:
            for c in range(1, len(data)):
                if len(data[0]) != len(data[c]):
                    raise Exception('All lines must have the same number of objects.')
            return True
        else:
            raise Exception('Invalid value for "data". You must pass a list of Line\'s.')

    def __setitem__(self, key, value):
        self._board[key] = value

    def __getitem__(self, item):
        return self._board[item]

    def __str__(self):
        return self._impress()

    def __repr__(self):
        return str(self._board)
