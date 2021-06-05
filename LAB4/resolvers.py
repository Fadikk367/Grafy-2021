from graphs.Graph import Graph, AdjacencyMatrix
from graphs.Algorithms import Algorithms
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
	result = am.Kosaraju()
	return result


def random_strongly_connected_component_resolver(data, _):
	def random_matrix(n, p):
		adj_matrix = [['.']*n for i in range(n)]

		for i in range(n):
			for j in range(n):
				if i != j and random.random() < p:
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
	for i in range(n):
		for j in range(n):
			if adj_matrix.matrix[i][j] == 1:
				adj_matrix.matrix[i][j] = random.choice(numbers)
	return adj_matrix


def bellman_ford_resolver(graph: Graph, args):
	try:
		dist, pred = graph.BellmanFord()
	except Exception as e:
		return str(e)

	ret = "Tablica odległości: \n"
	ret += str(dist) + "\n\n"


	ret += "Ścieżki: \n"
	for i in range(len(pred)):
		if pred[i] is None:
			pass
		current = i
		path = []
		while current != None:
			path.append(current)
			current = pred[current]
		ret += f'{i}: '
		path = path[::-1]
		for v in path:
			ret += f'({v}) '
		ret += f'\n'


	return ret


def johnson_resolver(graph, _):
	try:
		result = Algorithms.johnson(graph)

		result_str = ""
		for row in result:
			result_str += f"{'  '.join([f' {cell}' if len(str(cell)) == 1 else f'{cell}' for cell in row])}\n"

		return result_str
	except Exception as e:
		return str(e)
