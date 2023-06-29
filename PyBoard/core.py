from .board_components import Line


class Board:
    def __init__(self, n_lines: int, n_columns: int, data: list = None, blank_spaces: bool = False):
        self._n_lines = n_lines
        self._n_columns = n_columns
        self.blank_spaces = blank_spaces
        if data:
            self._board = data
        else:
            self._board = self._build_board()

    def _build_board(self):
        board = []
        for lin in range(0, self._n_lines):
            line = Line()
            for col in range(0, self._n_columns):
                line.append(None)
            board.append(line)
        return board

    def numerate(self):
        i = -1
        for line in self._board:
            i += 1
            j = -1
            for item in line:
                j += 1
                if item is None:
                    self._board[i][j] = f'{i}{j}'

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
