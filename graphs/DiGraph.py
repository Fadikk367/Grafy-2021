import copy


class DiGraph:
    def __init__(self, size):
        self.adj_matrix = [[0 for el in range(size)] for el in range(size)]
        self.adj_list = [[] for el in range(size)]
        self.inc_matrix = [[] for el in range(size)]

    def add_edge(self, start_v, end_v):
        self.adj_list[start_v].append(end_v)
        self.adj_matrix[start_v][end_v] = 1
        for idx, el in enumerate(self.inc_matrix):
            if idx == start_v:
                el.append(1)
            elif idx == end_v:
                el.append(-1)
            else:
                el.append(0)

    def with_adj_matrix(self, adj_matrix):
        self.adj_matrix = adj_matrix
        self.adj_list = [[idx for idx, val in enumerate(el) if val] for el in adj_matrix]
        self.inc_matrix = adj_matrix_to_incidence_matrix(adj_matrix)

    def from_adj_list(self, adj_list):
        self.adj_list = adj_list
        size = range(len(adj_list))
        self.adj_matrix = [[1 if i in el else 0 for i in size] for el in adj_list]
        self.inc_matrix = adj_matrix_to_incidence_matrix(self.adj_matrix)

    def from_file(self, filename):
        with open(filename) as f:
            adj_matrix = [[int(num) for num in line.split(' ')] for line in f]
        self.with_adj_matrix(adj_matrix)

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

    def DFS_visit(self, v, d, f, t):
        t[0] += 1
        d[v] = t[0]
        for i in range(len(self.adj_matrix[v])):
            if d[i] == -1 and self.adj_matrix[v][i] == 1:
                self.DFS_visit(i, d, f, t)
        t[0] += 1
        f[v] = t[0]

    def Components_R(self, nr, v, comp):
        for i in range(len(self.adj_matrix[v])):
            if self.adj_matrix[v][i] == 1 and comp[i] == -1:
                comp[i] = nr
                self.Components_R(nr, i, comp)

    def transpose(self):
        tmp = DiGraph(len(self.adj_matrix))
        for i in range(len(self.adj_matrix)):
            for j in range(len(self.adj_matrix[i])):
                if self.adj_matrix[i][j] == 1:
                    tmp.add_edge(j, i)
        return tmp

    def Kosaraju(self):
        d = [-1 for i in range(len(self.adj_matrix))]
        f = copy.deepcopy(d)
        t = [0]
        for v in range(len(d)):
            if d[v] == -1:
                self.DFS_visit(v, d, f, t)
        transposed_graph = self.transpose()
        nr = 0
        comp = []
        for v in range(len(d)):
            comp.append(-1)

        nodes = [i for i in range(len(self.adj_matrix))]
        nodes_f_sorted_high_to_low = sorted(dict(zip(nodes, f)).items(), key=lambda kv: (-1 * kv[1], -1 * kv[0]))

        for i in nodes_f_sorted_high_to_low:
            if comp[i[0]] == -1:
                nr += 1
                comp[i[0]] = nr
                transposed_graph.Components_R(nr, i[0], comp)

        nodes_comp_sorted = sorted(dict(zip(nodes, comp)).items(), key=lambda kv: (kv[1], kv[0]))

        print("Silnie spojne skladowe grafu:")
        tmp = nodes_comp_sorted[0][1]
        for i in nodes_comp_sorted:
            if tmp == i[1]:
                print(i[0], " ", end="")
            else:
                print("")
                print(i[0], " ", end="")
            tmp = i[1]

        return comp


def adj_matrix_to_incidence_matrix(adj_matrix):
    inc_matrix = [[] for el in range(len(adj_matrix))]
    for idx_row, row in enumerate(adj_matrix):
        for idx_col, col in enumerate(row):
            if adj_matrix[idx_row][idx_col]:
                for idx, el in enumerate(inc_matrix):
                    if idx == idx_row:
                        el.append(1)
                    elif idx == idx_col:
                        el.append(-1)
                    else:
                        el.append(0)
    return inc_matrix
