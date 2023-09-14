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
    if visited is None:
        visited = set()
    visited.add(node)
    print(node)
    for next in set(data.get(node, [])) - visited:
        if next not in visited:
            my_code(data, next, visited)


my_code(data, 1)
my_code(data_2, 1)
my_code(data_3, 1)
