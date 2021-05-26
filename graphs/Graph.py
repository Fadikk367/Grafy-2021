from __future__ import annotations

import random
import copy

from typing import List, Set, Dict
from numpy.random import choice


class Node:
    """
    Representation of single node in a graph
    """
    def __init__(self, node_id: int = 0, visited: bool = False):
        self.id = node_id
        self.is_visited = visited

    def __eq__(self, other):
        # print('node')
        # print(self)
        # print(other)
        return self.id == other.id

    def __hash__(self) -> int:
        return id(self)

    def __str__(self):
        return f"({self.id})"


class Edge:
    """
    Representation of a two direction egde in a graph
    """
    def __init__(self, first_node: Node, second_node: Node, is_visited: bool = False, weight: int = 0, is_weighted: bool = False):
        self.nodes = (first_node, second_node)
        self.weight = weight
        self.is_visited = is_visited
        self.is_weighted = is_weighted

    def has_node(self, node: Node) -> bool:
        return self.nodes[0] == node or self.nodes[1] == node

    def __str__(self):
        if self.is_weighted:
            return f"{self.nodes[0]}-[{self.weight}]-{self.nodes[1]}"
        else:
            return f"{self.nodes[0]}--{self.nodes[1]}"

    def __eq__(self, other):
        # print('edge')
        # print(self)
        # print(other)
        return (
            (self.nodes[0] == other.nodes[0] and self.nodes[1] == other.nodes[1]) or
            (self.nodes[1] == other.nodes[0] and self.nodes[0] == other.nodes[1])
        )

    def has_common_node_with(self, other) -> bool:
        return any([
            self.nodes[0] == other.nodes[0],
            self.nodes[0] == other.nodes[1],
            self.nodes[1] == other.nodes[0],
            self.nodes[1] == other.nodes[1]
        ])


class Graph:
    """
    Graph representation as a set of nodes and list of edges
    """
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
                if value != 0:
                    # edges.append(Edge(Node(i), Node(j)))
                    edges.append(Edge(Node(i), Node(j), weight=value, is_weighted=True))

        return Graph(edges, nodes)

    @staticmethod
    def from_cost_matrix(cost_matrix) -> Graph:
        nodes = set([Node(i) for i in range(len(cost_matrix[0]))])
        edges = []

        for i, _ in enumerate(cost_matrix):
            for j, value in enumerate(cost_matrix[i]):
                if value > 0 and j > i:
                    edges.append(Edge(Node(i), Node(j), weight=value, is_weighted=True))

        return Graph(edges, nodes)

    @staticmethod
    def from_file(path) -> Graph:
        adjacency_matrix = []

        with open(path, 'r') as file:
            rows = file.read().split('\n')

            for row in rows:
                if row:
                    adjacency_matrix.append([int(cell) for cell in row.split(' ')])

        return Graph.from_adjacency_matrix(adjacency_matrix)

    def __str__(self):
        separator = ", "
        nodes_string = separator.join(str(node) for node in self.nodes)
        edges_string = separator.join(str(edge) for edge in self.edges)

        return nodes_string + "\n" + edges_string

    def add_node(self, node: Node):
        self.nodes.add(node)

    def remove_node(self, node: Node):
        self.nodes.remove(node)

    def add_edge(self, edge: Edge):
        self.edges.append(edge)

    def remove_edge(self, edge: Edge):
        self.edges.remove(edge)

    def has_edge(self, edge: Edge) -> bool:
        return edge in self.edges

    def get_edge_with_nodes(self, node_a_id: int, node_b_id: int):
        for edge in self.edges:
            potential_edge = Edge(Node(node_a_id), Node(node_b_id))

            if edge == potential_edge:
                return edge

        return None

    def get_neighbours(self, node_id: Node) -> List[Node]:
        neighbours = []
        for edge in self.edges:
            if edge.nodes[0].id == node_id:
                neighbours.append(edge.nodes[1])
            elif edge.nodes[1].id == node_id:
                neighbours.append(edge.nodes[0])

        return neighbours

    def randomize(self, permutations=5):
        for i in range(permutations):
            it = 100
            while it > 0:
                it -= 1
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

            if it == 0:
                raise Exception('Graph cannot be randomized')

    def BellmanFord(self, start_node=0):
        d = [float("Inf")] * len(self.nodes)
        d[start_node] = 0

        for _ in range(len(self.nodes) - 1):
            for edge in self.edges:
                node1 = edge.nodes[0]
                node2 = edge.nodes[1]
                weight = edge.weight
                if d[node1.id] != float("Inf") and d[node1.id] + weight < d[node2.id]:
                    d[node2.id] = d[node1.id] + weight


        for edge in self.edges:
            node1 = edge.nodes[0]
            node2 = edge.nodes[1]
            weight = edge.weight
            if d[node1.id] != float("Inf") and d[node1.id] + weight < d[node2.id]:
                return "There is a negative weight cycle!"

        return d


class AdjacencyList:
    """
    Graph representation as a adjacency list
    """
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
    """
    Graph representation as a adjacency matrix
    """
    def __init__(self, graph: Graph, is_digraph=False):
        dimension = len(graph.nodes)

        self.matrix = [[0]*dimension for i in range(dimension)]

        if not is_digraph:
            for edge in graph.edges:
                (start, end) = edge.nodes
                #self.matrix[start.id][end.id] = 1 if not edge.is_weighted else edge.weight
                #self.matrix[end.id][start.id] = 1 if not edge.is_weighted else edge.weight
                
                self.matrix[start.id][end.id] = edge.weight
                self.matrix[end.id][start.id] = edge.weight
        else:
            for edge in graph.edges:
                (start, end) = edge.nodes
                self.matrix[start.id][end.id] = edge.weight

    def __str__(self):
        stringified = ""

        for row in self.matrix:
            stringified += " ".join([str(i) for i in row]) + "\n"

        return stringified

    def random_digraph(self, n, p):
        self.matrix = [[0 for el in range(n)] for el in range(n)]
        for idx_row, row in enumerate(self.matrix):
            for idx_col, col in enumerate(row):
                if idx_row != idx_col:
                    self.matrix[idx_row][idx_col] = int(choice([0, 1], 1, p=(1 - p, p)))
        return self

    def DFS_visit(self, v, d, f, t):
        t[0] += 1
        d[v] = t[0]
        for i in range(len(self.matrix[v])):
            if d[i] == -1 and self.matrix[v][i] == 1:
                self.DFS_visit(i, d, f, t)
        t[0] += 1
        f[v] = t[0]

    def Components_R(self, nr, v, comp):
        for i in range(len(self.matrix[v])):
            if self.matrix[v][i] == 1 and comp[i] == -1:
                comp[i] = nr
                self.Components_R(nr, i, comp)

    def transpose(self):
        n = len(self.matrix[0])
        tmp_matrix = [[0]*n for i in range(n)]
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if self.matrix[i][j] == 1:
                    tmp_matrix[j][i] = 1
        graph = Graph()
        am = AdjacencyMatrix(graph)
        am.matrix = tmp_matrix
        return am

    def Kosaraju(self):
        d = [-1 for i in range(len(self.matrix))]
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

        nodes = [i for i in range(len(self.matrix))]
        nodes_f_sorted_high_to_low = sorted(dict(zip(nodes, f)).items(), key=lambda kv: (-1 * kv[1], -1 * kv[0]))

        for i in nodes_f_sorted_high_to_low:
            if comp[i[0]] == -1:
                nr += 1
                comp[i[0]] = nr
                transposed_graph.Components_R(nr, i[0], comp)

        nodes_comp_sorted = sorted(dict(zip(nodes, comp)).items(), key=lambda kv: (kv[1], kv[0]))

        tmp = nodes_comp_sorted[0][1]
        result = ""
        for i in nodes_comp_sorted:
            if tmp == i[1]:
                result += f'{i[0]} '
            else:
                result += f'\n{i[0]} '
            tmp = i[1]

        return result


