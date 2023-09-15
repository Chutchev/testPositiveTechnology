data = {
    'first': 'first_value',
    'second': 'second_value'
}
data_2 = {
    '1': {
        'child': '1/child/value',
    },
    '2': '2/value'
}

data_3 = {
    '1': {
        'child': '1/child/value',
    },
    '2': '2/value',
    '3': {
        'child': '1/child/value',
        'child_2': '21/child/value'
    }
}
data_4 = {
    '1': {
        'child': '1/child/value',
    },
    '2': ('2/value', '1'),
    '3': {
        'child': '1/child/value',
        'child_2': '21/child/value'
    }
}

data_5 = {
    '1': {
        'child': '1/child/value',
    },
    '2': ('2/value', '1'),
    '3': {
        'child': '1/child/value',
        'child_2': '21/child/value'
    },
    '4': True,
    '5': [{
        'child': '1/child/value',
    }, {
        'child': '1/child/value',
    }]
}


# Предположил что списки/кортежи/множества тоже могут быть значениями.
def my_code(data: dict, level=0):
    """
    Функция, выводит на экран словарь по уровням вложенности.
    :param data: словарь
    :param level: текущий уровень вложенности. По-умолчанию - 0
    :return: None
    """
    for k, v in data.items():
        tabulation = "\t" * level
        print(f"{tabulation}{k}:")
        if isinstance(v, dict):
            my_code(v, level + 1)
        elif isinstance(v, (list, tuple, set)):
            tabulation += "\t"
            for el in v:
                if isinstance(el, dict):
                    my_code(el, level + 1)
                else:
                    print(f"{tabulation}{el}")
        else:
            tabulation += "\t"
            print(f"{tabulation}{v}")
