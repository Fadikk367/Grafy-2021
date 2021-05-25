from numpy.random import choice


class RandomDiGraph:
    def __init__(self, n, p):
        self.adj_matrix = [[0 for el in range(n)] for el in range(n)]
        self.inc_matrix = [[] for i in range(n)]
        for idx_row, row in enumerate(self.adj_matrix):
            for idx_col, col in enumerate(row):
                if idx_row != idx_col:
                    self.adj_matrix[idx_row][idx_col] = int(choice([0, 1], 1, p=(1 - p, p)))
                    if self.adj_matrix[idx_row][idx_col]:
                        for idx, el in enumerate(self.inc_matrix):
                            if idx == idx_row:
                                el.append(1)
                            elif idx == idx_col:
                                el.append(-1)
                            else:
                                el.append(0)
        self.adj_list = [[idx for idx, val in enumerate(el) if val] for el in self.adj_matrix]

    def print(self):
        print('Adjacency Matrix:')
        for row in self.adj_matrix:
            print(row)
        print('\nAdjacency list:')
        for idx, li in enumerate(self.adj_list):
            print(f"{idx}: {li}")
        print('\nIncidence Matrix:')
        for row in self.inc_matrix:
            print(row)


if __name__ == "__main__":
    graph = RandomDiGraph(7, 0.2)
    graph.print()
