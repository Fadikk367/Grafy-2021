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
        for edge in graph.edges:
            (first_node, second_node) = edge.nodes

            self.list[first_node.id].append(second_node)
            self.list[second_node.id].append(first_node)

    def remove_edge(self, edge: Edge):
        (first_node, second_node) = edge.nodes
        for i, key in enumerate(self.list[first_node.id]):
            if key == second_node:
                self.list[first_node.id].pop(i)
        for i, key in enumerate(self.list[second_node.id]):
            if key == first_node:
                self.list[second_node.id].pop(i)

    def add_edge(self, edge: Edge):
        (first_node, second_node) = edge.nodes
        self.list[first_node.id].append(second_node)
        self.list[second_node.id].append(first_node)

    def DFSCount(self, node1, visited):
        count = 1
        visited[node1.id] = True
        for i in self.list[node1.id]:
            if visited[i.id] == False:
                count += self.DFSCount(i, visited)
        return count

    def isValidNextEdge(self, node1, node2):
        if len(self.list[node1.id]) == 1:
            return True
        else:
            visited = [False]*len(self.list)
            count1 = self.DFSCount(node1, visited)
            self.remove_edge(Edge(node1, node2))
            visited = [False]*len(self.list)
            count2 = self.DFSCount(node1, visited)
            self.add_edge(Edge(node1, node2))
            return count1 <= count2

    def find_euler_path(self, node1):
        for node2 in self.list[node1.id]:
            if self.isValidNextEdge(node1, node2):
                print("%d-%d " %(node1.id, node2.id)),
                self.remove_edge(Edge(node1, node2))
                self.find_euler_path(node2)



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

