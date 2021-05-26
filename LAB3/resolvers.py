from graphs.Graph import Node, Edge, Graph, AdjacencyMatrix
from graphs.Algorithms import Algorithms
import random


def random_weighted_graph_resolver(data, _):
	def random_matrix(size, p):
		adj_matrix = [[0]*size for i in range(size)]

		for i in range(size):
			for j in range(i, size):
				if i != j and random.random() < p:
					# 0.4 - probability that edge between i and j exists
					adj_matrix[i][j] = adj_matrix[j][i] = 1
		return adj_matrix

	size = int(data.split(' ')[0])
	p = float(data.split(' ')[1])
	if size < 0:
		return "Size cannot be a negative number"
	adj_matrix = random_matrix(size, p)
	graph = Graph.from_adjacency_matrix(adj_matrix)
	components = Algorithms.max_connected_comp(graph)
	while len(components) > 1:
		adj_matrix = random_matrix(size, p)
		graph = Graph.from_adjacency_matrix(adj_matrix)
		components = Algorithms.max_connected_comp(graph)

	for i in range(size):
		for j in range(i, size):
			if adj_matrix[i][j] == 1:
				adj_matrix[i][j] = adj_matrix[j][i] = random.randrange(1, 11)
	graph = Graph.from_adjacency_matrix(adj_matrix)
	am = AdjacencyMatrix(graph)
	return am


