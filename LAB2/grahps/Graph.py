from __future__ import annotations

import random

from typing import List, Set, Dict


class Node:
    id: int
    is_visited: bool

    def __init__(self, node_id: int = 0, visited: bool = False):
        self.id = node_id
        self.is_visited = visited

    def __eq__(self, other):
        # isinstance(other, self.__class__)
        return self.id == other.id

    def __hash__(self) -> int:
        return id(self)

    def __str__(self):
        return f"({self.id})"


class Edge:
    def __init__(self, first_node: Node, second_node: Node, is_visited: bool = False, weight: int = 0, is_weighted: bool = False):
        self.nodes = (first_node, second_node)
        self.weight = weight
        self.is_visited = is_visited
        self.is_weighted = is_weighted

    def __str__(self):
        return f"{self.nodes[0]}--{self.nodes[1]}"

    def __eq__(self, other):
        # TODO
        # return (
        #     (self.nodes[0] == other.nodes[0] and self.nodes[1] == other.nodes[1]) or
        #     (self.nodes[1] == other.nodes[0] and self.nodes[0] == other.nodes[1])
        # )
        return self.nodes[0] == other.nodes[0] and self.nodes[1] == other.nodes[1]

    def has_common_node_with(self, other) -> bool:
        return (
            self.nodes[0] == other.nodes[0] or
            self.nodes[0] == other.nodes[1] or
            self.nodes[1] == other.nodes[0] or
            self.nodes[1] == other.nodes[1]
        )


class Graph:
    def __init__(self, edges: List[Edge] = None, nodes: Set[Node] = None):
        self.edges = edges if edges is not None else []
        self.nodes = nodes if nodes is not None else set()

    @staticmethod
    def from_adjacency_list(adjacency_list) -> Graph:
        graph = Graph()

        for node_id, neighbours in adjacency_list.list.items():
            new_node = Node(node_id)
            graph.add_node(new_node)

            for neighbour in neighbours:
                new_edge = Edge(new_node, neighbour)

                if not graph.has_edge(new_edge):
                    graph.add_edge(new_edge)

        return graph

    @staticmethod
    def from_adjacency_matrix(adjacency_matrix) -> Graph:
        nodes = set([Node(i) for i in range(len(adjacency_matrix.matrix[0]))])

        edges = []

        for i, _ in enumerate(adjacency_matrix.matrix):
            for j, value in enumerate(adjacency_matrix.matrix[i]):

                if value == 1 and j > i:
                    edges.append(Edge(Node(i), Node(j)))

        return Graph(edges, nodes)

    def __str__(self):
        separator = ", "
        nodes_string = separator.join(str(node) for node in self.nodes)
        edges_string = separator.join(str(edge) for edge in self.edges)

        return nodes_string + "\n" + edges_string

    def add_node(self, node: Node):
        self.nodes.add(node)

    def add_edge(self, edge: Edge):
        self.edges.append(edge)

    def remove_edge(self, edge: Edge):
        self.edges.remove(edge)

    def has_edge(self, edge: Edge) -> bool:
        return edge in self.edges

    def randomize(self, permutations):
        for i in range(permutations):
            while True:
                (edge_a, edge_b) = random.sample(self.edges, 2)

                are_edges_separated = not edge_a.has_common_node_with(edge_b)

                (node_a_first, node_a_second) = edge_a.nodes
                (node_b_first, node_b_second) = edge_b.nodes

                new_edge_a = Edge(node_a_first, node_b_second)
                new_edge_b = Edge(node_a_second, node_b_first)

                are_new_edges_not_duplicated = not self.has_edge(new_edge_a) and not self.has_edge(new_edge_b)

                if are_edges_separated and are_new_edges_not_duplicated:
                    self.remove_edge(edge_a)
                    self.remove_edge(edge_b)

                    self.add_edge(new_edge_a)
                    self.add_edge(new_edge_b)

                    break

    def hamiltonian_cycle(self, graph, v=0, cycle=None):
        if cycle is None:
            cycle = []

        nodes = AdjacencyList(graph).list

        # if v not in set(cyc)



class AdjacencyList:
    def __init__(self, graph: Graph):
        self.list = {key.id: [] for key in graph.nodes}
        print(self.list)
        for edge in graph.edges:
            (first_node, second_node) = edge.nodes

            self.list[first_node.id].append(second_node)
            self.list[second_node.id].append(first_node)


class AdjacencyMatrix:
    def __init__(self, graph: Graph):
        dimension = len(graph.nodes)

        self.matrix = [[0]*dimension for i in range(dimension)]

        for edge in graph.edges:
            (start, end) = edge.nodes
            self.matrix[start.id][end.id] = 1
            self.matrix[end.id][start.id] = 1

    def __str__(self):
        stringified = ""

        for row in self.matrix:
            stringified += " ".join([str(i) for i in row]) + "\n"

        return stringified



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
    print(AdjacencyMatrix(graph))

    # adjacency_matrix = AdjacencyMatrix(graph)
    # print(adjacency_matrix)
    #
    # restored = Graph.from_adjacency_matrix(adjacency_matrix)
    # print(restored)
    # graph.randomize(5)
    # print(AdjacencyMatrix(graph))
    adj_list = AdjacencyList(graph)

    restored = Graph.from_adjacency_list(adj_list)

    print(restored)

    # for node in adj_list.list:
    #     print(str(node) + str([str(n) for n in adj_list.list[node]]))

