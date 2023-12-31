class Line:
    def __init__(self, data: list = None):
        """
        param data: define line directly
        """
        if not data:
            self.line = []
        else:
            if type(data) == list:
                self.line = data
            else:
                raise Exception(f'"data" must be a list. You passed {type(data)} instead')
        self.index = -1
        self.closed = False

    def close(self):
        """
        The list will not receive more elements.
        """
        self.closed = True

    def open(self):
        """
        The list is open for new elements.
        """
        self.closed = False

    def append(self, obj):
        """
        Append only if the list is open.
        """
        if not self.closed:
            self.line.append(obj)
        else:
            raise Exception(f'The Line is closed. It can\' receive more elements.')

    def __setitem__(self, key, value):
        self.line[key] = value

    def __getitem__(self, item):
        try:
            return self.line[item]
        except IndexError:
            return None

    def __next__(self):
        if self.index == len(self.line) - 1:
            self.index = -1
            raise StopIteration
        self.index += 1
        return self.line[self.index]

    def __iter__(self):
        return self

    def __repr__(self):
        return str(self.line)

    def __len__(self):
        return len(self.line)
