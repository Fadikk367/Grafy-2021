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
        return (
            (self.nodes[0] == other.nodes[0] and self.nodes[1] == other.nodes[1]) or
            (self.nodes[1] == other.nodes[0] and self.nodes[0] == other.nodes[1])
        )
        # return self.nodes[0] == other.nodes[0] and self.nodes[1] == other.nodes[1]

    def has_common_node_with(self, other) -> bool:
        # return (
        #     self.nodes[0] == other.nodes[0] or
        #     self.nodes[0] == other.nodes[1] or
        #     self.nodes[1] == other.nodes[0] or
        #     self.nodes[1] == other.nodes[1]
        # )

        return any([
            self.nodes[0] == other.nodes[0],
            self.nodes[0] == other.nodes[1],
            self.nodes[1] == other.nodes[0],
            self.nodes[1] == other.nodes[1]
        ])


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
        nodes = set([Node(i) for i in range(len(adjacency_matrix[0]))])

        edges = []

        for i, _ in enumerate(adjacency_matrix):
            for j, value in enumerate(adjacency_matrix[i]):

                if value == 1 and j > i:
                    edges.append(Edge(Node(i), Node(j)))

        return Graph(edges, nodes)

    @staticmethod
    def from_file(path) -> Graph:
        adjacency_matrix = []

        with open(path, 'r') as file:
            rows = file.read().split('\n')

            for row in rows:
                adjacency_matrix.append([int(cell) for cell in row.split(' ')])

        return Graph.from_adjacency_matrix(adjacency_matrix)

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

    def randomize(self, permutations=5):
        for i in range(permutations):
            it = 100
            while it > 0:
                it -= 1
                (edge_a, edge_b) = random.sample(self.edges, 2)
                # print(f"\n{iter}) selected edges:")
                # print(str(edge_a) + ", " + str(edge_b))

                are_edges_separated = not edge_a.has_common_node_with(edge_b)
                # print("are separated:")
                # print(are_edges_separated)

                (node_a_first, node_a_second) = edge_a.nodes
                (node_b_first, node_b_second) = edge_b.nodes

                new_edge_a = Edge(node_a_first, node_b_second)
                new_edge_b = Edge(node_a_second, node_b_first)
                # print("New edges:")
                # print(str(new_edge_a) + ", " + str(new_edge_b))

                are_new_edges_not_duplicated = not self.has_edge(new_edge_a) and not self.has_edge(new_edge_b)
                # print("Is first edge duplicated:")
                # print(self.has_edge(new_edge_a))
                # print("Is second edge duplicated:")
                # print(self.has_edge(new_edge_b))

                if are_edges_separated and are_new_edges_not_duplicated:
                    self.remove_edge(edge_a)
                    self.remove_edge(edge_b)

                    self.add_edge(new_edge_a)
                    self.add_edge(new_edge_b)

                    break

            if it == 0:
                raise Exception('Graph cannot be randomized')

    @staticmethod
    def hamiltonian_cycle(graph, v=None, cycle=None):
        adjacency_list = AdjacencyList(graph)
        nodes = adjacency_list.get_nodes()

        if cycle is None:
            cycle = []
        if v is None:
            v = nodes[0]

        # print(f"current node: {v}")
        if v not in set(cycle):
            cycle.append(v)
            # print(f"visit {v}")

            if len(cycle) == len(nodes): # we have a hamilton's path
                closing_edge = Edge(Node(cycle[0]), Node(cycle[-1]))

                if graph.has_edge(closing_edge): # check if there is an connection between last node in path and start node
                    cycle.append(cycle[0])
                    return cycle
                else:
                    cycle.pop()
                    return None
            else:
                # print(f"v neighbours: {adjacency_list.get_neighbours(v)}")
                for neighbour in adjacency_list.get_neighbours(v):
                    cycle_copy = cycle[:]
                    hamiltonian_candidate = Graph.hamiltonian_cycle(graph, neighbour, cycle_copy)
                    if hamiltonian_candidate is not None:
                        return hamiltonian_candidate


class AdjacencyList:
    def __init__(self, graph: Graph):
        self.list = {key.id: [] for key in graph.nodes}

        for edge in graph.edges:
            (first_node, second_node) = edge.nodes

            self.list[first_node.id].append(second_node)
            self.list[second_node.id].append(first_node)

    def get_nodes(self):
        return list(self.list.keys())

    def get_neighbours(self, node_id):
        return [node.id for node in self.list[node_id]]

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

    def find_euler_path(self, node1, result=None):
        if result is None:
            result = []
        for node2 in self.list[node1.id]:
            if self.isValidNextEdge(node1, node2):
                result.append(f"({node1.id}-{node2.id})")
                self.remove_edge(Edge(node1, node2))
                self.find_euler_path(node2, result)

        return ", ".join(result)


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
    # A = Node(0)
    # B = Node(1)
    # C = Node(2)
    # D = Node(3)
    # E = Node(4)
    # nodes = {A, B, C, D, E}
    #
    # a = Edge(A, B)
    # b = Edge(B, C)
    # c = Edge(C, D)
    # d = Edge(D, E)
    # # e = Edge(E, A)
    # edges = [a, b, c, d]

    # graph = Graph(edges, nodes)
    graph = Graph.from_file('matrix.txt')
    print(graph)
    print(AdjacencyMatrix(graph))

    print(Graph.hamiltonian_cycle(graph))
    #
    # adj_list = AdjacencyList(graph)
    # for node in adj_list.list:
    #     print(str(node) + str([str(n) for n in adj_list.list[node]]))

    # adjacency_matrix = AdjacencyMatrix(graph)
    # print(adjacency_matrix)
    #
    # restored = Graph.from_adjacency_matrix(adjacency_matrix)
    # print(restored)
    # graph.randomize(100)
    # print(AdjacencyMatrix(graph))
    #
    # restored = Graph.from_adjacency_list(adj_list)

    # print(restored)
    # print(AdjacencyMatrix(graph))



