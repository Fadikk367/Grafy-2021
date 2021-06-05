from graphs.Graph import Graph, AdjacencyMatrix
from graphs.Algorithms import Algorithms
import random


def random_weighted_graph_resolver(data, _):
	def random_matrix(size, p):
		adj_matrix = [['.']*size for i in range(size)]

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
	matrix = random_matrix(size, p)
	graph = Graph.from_cost_matrix(matrix)
	components = Algorithms.max_connected_comp(graph)
	while len(components) > 1:
		matrix = random_matrix(size, p)
		graph = Graph.from_cost_matrix(matrix)
		components = Algorithms.max_connected_comp(graph)

	for i in range(size):
		for j in range(i, size):
			if matrix[i][j] == 1:
				matrix[i][j] = matrix[j][i] = random.randrange(1, 11)
	s = ""
	for row in matrix:
		s += f"{'  '.join([f' {cell}' if len(str(cell)) == 1 else f'{cell}' for cell in row])}\n"

	return s


def dijkstra_resolver(graph, _):
	d_s, p_s = Algorithms.dijkstra(graph, 0)

	result = ""
	for node, distance in enumerate(d_s):
		prev = p_s[node]
		path = [str(node)]

		while prev is not None:
			path.append(str(prev))
			prev = p_s[prev]

		path.reverse()
		result += f"d({node}) = {distance}, path: [{' - '.join(path)}]\n"

	return result


def distance_matrix_resolver(graph, _):
	result = Algorithms.distance_matrix(graph)
	s = ""

	for row in result:
		s += f"{'  '.join([f' {cell}' if len(str(cell)) == 1 else f'{cell}' for cell in row])}\n"

	return s


def center_resolver(graph, _):
	center, min_row_sum = Algorithms.graph_center(graph)
	center_minimax, minimax_distance = Algorithms.graph_minimax_center(graph)

	return f"center node id: {center} with sum of {min_row_sum}\nminimax center node id: {center_minimax} with minimax distance of {minimax_distance}\n"


def kruskal_resolver(graph, _):
	minimal_spanning_tree = Algorithms.kruskal(graph)

	result_str = ""
	for row in minimal_spanning_tree:
		result_str += f"{'  '.join([f' {cell}' if len(str(cell)) == 1 else f'{cell}' for cell in row])}\n"

	return result_str

