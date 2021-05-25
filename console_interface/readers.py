from graphs.Graph import Graph


def adjacency_matrix(filename):
    return Graph.from_file(filename)


def cost_matrix(filename):
    with open(filename) as f:
        data = f.read()

        matrix = []

        for row in data.split('\n'):
            if row:
                matrix.append([int(cell) for cell in row.split(' ')])

        return Graph.from_cost_matrix(matrix)


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

