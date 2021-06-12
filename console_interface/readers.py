import re

from graphs.Graph import Graph
from graphs.Algorithms import Algorithms
from .errors import Error


def parse_matrix(data):
    matrix = []

    for line in data.split('\n'):
        if line:
            tokens = re.split('\s+', line)
            row = []
            for token in tokens:
                if len(token) > 0:
                    if token == '.':
                        row.append(float('Inf'))
                    else:
                        row.append(int(token))

            matrix.append(row)

    return matrix


def graphical_sequence():
    data = input('Enter number sequence:\n')
    sequence = [int(number) for number in data.split(' ')]

    graph = Algorithms.degree_seq_to_graph(sequence)

    if graph is None:
        raise Error("Given sequence does not represent a valid graph")

    return graph


def adjacency_matrix(filename):
    with open(filename, 'r') as file:
        data = file.read()

        adj_matrix = parse_matrix(data)
        return Graph.from_adjacency_matrix(adj_matrix)


def directed_adjacency_matrix(filename):
    with open(filename, 'r') as file:
        data = file.read()

        adj_matrix = parse_matrix(data)
        return Graph.from_adjacency_matrix(adj_matrix, is_directed=True)


def cost_matrix(filename):
    with open(filename) as f:
        data = f.read()

        cost_mat = parse_matrix(data)
        return Graph.from_cost_matrix(cost_mat)


def directed_cost_matrix(filename):
    with open(filename) as f:
        data = f.read()

        dir_cost_mat = parse_matrix(data)
        return Graph.from_cost_matrix(dir_cost_mat, is_directed=True)


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

