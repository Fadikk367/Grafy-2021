from graphs.Algorithms import Algorithms
from graphs.Graph import Node, Edge, Graph, AdjacencyMatrix, AdjacencyList
import random


if __name__ == '__main__':
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


	# for node in adj_list.list:
	#     print(str(node) + str([str(n) for n in adj_list.list[node]]))
	
	#print(Algorithms.degree_seq_to_graph([1, 1, 1, 1]))

	print("\n\n")
	eulerian_graph = Algorithms.create_random_eulerian2(5)
	print(eulerian_graph)

	AdjacencyList.find_euler_path(AdjacencyList(eulerian_graph), Node(0))
