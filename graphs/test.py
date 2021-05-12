from Graph import Graph, Node, Edge
from representations.AdjacencyMatrix import AdjacencyList

if __name__ == "__main__":
    A = Node(0)
    B = Node(1)
    C = Node(2)
    D = Node(3)
    E = Node(4)
    nodes = {A, B, C, D, E}

    a = Edge(A, B)
    b = Edge(A, C)
    c = Edge(A, D)
    d = Edge(A, E)
    e = Edge(D, E)
    edges = [a, b, c, d, e]

    graph = Graph(edges, nodes)
    print(graph)
    graph.randomize(3)
    print(graph)
    adj_list = AdjacencyList(graph)
    print(adj_list.list)