from graphs.Graph import Graph, AdjacencyMatrix
import random


def random_digraph_resolver(data, _):
	n = int(data.split(' ')[0])
	p = float(data.split(' ')[1])

	graph = Graph()
	am = AdjacencyMatrix(graph)
	am.random_digraph(n, p)

	return am


def kosaraju_resolver(graph: Graph, args):
	am = AdjacencyMatrix(graph, is_digraph=True)
	print(am.Kosaraju())
	return graph


def random_strongly_connected_component_resolver(data, _):
	def random_matrix(n, p):
		adj_matrix = [[0]*n for i in range(n)]

		for i in range(n):
			for j in range(n):
				if i != j and random.random() < p:
					# 0.4 - probability that edge between i and j exists
					adj_matrix[i][j] = 1
		return adj_matrix

	n = int(data.split(' ')[0])
	p = float(data.split(' ')[1])

	if n < 0:
		return "Size cannot be a negative number"
	if p < 0 or p > 1:
		return "Probability not in range [0, 1]"
	graph = Graph()
	adj_matrix = AdjacencyMatrix(graph)
	adj_matrix.matrix = random_matrix(n, p)
	components = adj_matrix.Kosaraju().split('\n')
	while len(components) > 1:
		adj_matrix.matrix = random_matrix(n, p)
		components = adj_matrix.Kosaraju().split('\n')

	numbers = list(range(-5, 11))
	numbers.remove(0)
	for i in range(n):
		for j in range(n):
			if adj_matrix.matrix[i][j] == 1:
				adj_matrix.matrix[i][j] = random.choice(numbers)
	return adj_matrix


def bellman_ford_resolver(graph: Graph, args):
	print(graph)
	return graph.BellmanFord()
