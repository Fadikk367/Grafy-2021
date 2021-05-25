from graphs.DiGraph import DiGraph, adj_matrix_to_incidence_matrix


if __name__ == '__main__':
    graph = DiGraph(5)
    # adj_l = [
    #     [1, 4],
    #     [2],
    #     [3, 0],
    #     [1, 0],
    #     [2, 3]
    # ]
    # graph.from_adj_list(adj_l)
    graph.from_file('test.in')
    # graph.add_edge(0, 3)
    graph.print()
