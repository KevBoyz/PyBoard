from .board_components import Line


class Board:
    def __init__(self, n_lines: int = None, n_columns: int = None, data: list = None, blank_spaces: bool = False):
        self._n_lines = n_lines
        self._n_columns = n_columns
        self._board = None
        self.blank_spaces = blank_spaces
        # Define Board
        if data:
            self._board = data
            if not self._n_lines or self._n_columns:
                self._n_lines, self._n_columns = self.get_dims()
        elif self._n_lines and self._n_columns:
            self._build()
        else:
            raise Exception('The board is empty')


    def _build(self):
        board = []
        for lin in range(0, self._n_lines):
            line = Line()
            for col in range(0, self._n_columns):
                line.append(None)
            board.append(line)
        self._board = board

    def numerate(self):
        i = -1
        for line in self._board:
            i += 1
            j = -1
            for item in line:
                j += 1
                if item is None:
                    self._board[i][j] = f'{i}{j}'

    def get_dims(self):
        row_conter = 0
        longer_row = []
        for row in self._board:
            row_conter += 1
            if len(row) > len(longer_row):
                longer_row = row
        column_conter = len(longer_row)
        return row_conter, column_conter



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

    def __setitem__(self, key, value):
        self._board[key] = value

    def __getitem__(self, item):
        return self._board[item]

    def __str__(self):
        return self._impress()

    def __repr__(self):
        return str(self._board)
