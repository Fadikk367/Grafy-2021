from graphs.Graph import Graph


def adjacency_matrix(filename):
    adj_matrix = []

    with open(filename, 'r') as file:
        rows = file.read().split('\n')

        for row in rows:
            if row:
                adj_matrix.append([int(cell) for cell in row.split(' ')])

    return Graph.from_adjacency_matrix(adj_matrix)


def directed_adjacency_matrix(filename):
    adj_matrix = []

    with open(filename, 'r') as file:
        rows = file.read().split('\n')

        for row in rows:
            if row:
                adj_matrix.append([int(cell) for cell in row.split(' ')])

    return Graph.from_adjacency_matrix(adj_matrix, is_directed=True)


def cost_matrix(filename):
    with open(filename) as f:
        data = f.read()

        matrix = []

        for row in data.split('\n'):
            if row:
                matrix.append([int(cell) for cell in row.split(' ')])

        return Graph.from_cost_matrix(matrix)


def directed_cost_matrix(filename):
    with open(filename) as f:
        data = f.read()

        matrix = []

        for row in data.split('\n'):
            if row:
                matrix.append([int(cell) for cell in row.split(' ')])

        return Graph.from_cost_matrix(matrix, is_directed=True)


def incidence_matrix(filename):
    with open(filename) as f:
        data = f.read()

        matrix = []

        for row in data.split('\n'):
            matrix.append([int(cell) for cell in row.split(' ')])

    return data


def adjacency_list(filename):
    with open(filename) as f:
        data = f.read()

    return data


def plain(filename):
    with open(filename) as f:
        data = f.read()

    return data

