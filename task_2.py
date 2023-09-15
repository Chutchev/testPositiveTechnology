data = {
    1: [2, 3],
    2: [4]
}

data_2 = {
    1: [2, 3],
    2: [3, 4],
    4: [1]
}

data_3 = {
    1: [2, 3, 4, 5, 7],
    2: [3],
    4: [3, 5],
    6: [4],
    7: [6]
}


# Типичный обход графа в глубину
def my_code(data: dict, node: int, visited=None):
    """
    Функция, печатает достижимые вершины графа, начиная с заданной
    :param data: словарь вершин графа
    :param node: заданная нода
    :param visited: множество посещенных вершин
    :return: None
    """
    if visited is None:
        visited = set()
    visited.add(node)
    print(node)
    for next in set(data.get(node, [])) - visited:
        if next not in visited:
            my_code(data, next, visited)