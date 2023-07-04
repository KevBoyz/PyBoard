def set_columns(data):
    columns = []
    for c in range(0, len(data[0])):
        column = []
        for lin in data:
            column.append(lin[c])
        columns.append(column)
    return columns


def get_len(item):
    try:
        length = len(item)
    except TypeError:
        try:
            length = len(str(item))
        except Exception as e:
            raise Exception(f'Value {item} can not be read by len()\n', e)
    return length


def get_impress_config(cols):
    config = []
    for lin in cols:
        longer = get_len(max(lin))
        config.append([longer, longer % 2])
    return config


data = [
    [1000, 20],
    [10, 7],
    [1, 2],
    [10000, 2000],

]

cols = set_columns(data)
config = get_impress_config(cols)


def impress(data):
    impression = ''
    for n_line, lin in enumerate(data):
        for n_item, item in enumerate(lin):
            length = get_len(item)
            conf = config[n_item]
            dif = conf[0] - length
            if length < conf[0]:
                impression += f"{item}{dif * ' '} "
            else:
                impression += f'{item} '
        impression += '\n'
    print(impression)


impress(data)
