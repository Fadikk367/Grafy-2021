import digraph_test2
from LAB4.zad1 import RandomDigraph

if __name__ == '__main__':
    random_graph = RandomDigraph.RandomDiGraph(9, 0.2)
    random_graph.print()
    graph = digraph_test2.DiGraph(9)
    graph.with_adj_matrix(random_graph.adj_matrix)
    graph.Kosaraju()

    # graph = digraph.DiGraph(7)
    # graph.from_file('test.in')
    # graph.print()
    # print("")
    # graph.Kosaraju()

