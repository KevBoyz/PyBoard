def set_columns(data):
    columns = []
    for c in range(0, 5):
        column = []
        for lin in data:
            column.append(lin[c])
        columns.append(column)
    return columns


data = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10]
]

print(set_columns(data))
