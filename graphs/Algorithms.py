from .Graph import Graph, AdjacencyList, Node, Edge
import random, copy


class Algorithms:

	@staticmethod
	def is_degree_seq(Arr):
		A = Arr.copy()
		if Algorithms.count_odds(A)%2 == 1:
			return False
		A.sort(reverse=True)
		flag = False
		while True:
			flag = all(x == 0 for x in A)
			if flag:
				return flag
			if A[0] < 0 or A[0] >= len(A):
				return False
			for elem in A:
				if elem < 0:
					return False
			for i in range(1, A[0] + 1):
				A[i] -= 1
			A[0] = 0
			A.sort(reverse=True)

	@staticmethod
	def count_odds(Arr):
		count = 0
		for elem in Arr:
			if elem % 2 == 1:
				count += 1
		return count

	@staticmethod
	def degree_seq_to_graph(arr):
		a = arr.copy()
		a.sort(reverse=True)
		if not Algorithms.is_degree_seq(a):
			return None
		nodes = [Node(i) for i in range(len(a))]
		edges = []
		for i in range(len(a)):
			for j in range(i+1, len(a)):
				if a[i] > 0 and a[j] > 0:
					a[i] -= 1
					a[j] -= 1
					edges.append(Edge(nodes[i], nodes[j]))
		return Graph(edges, nodes)

	@staticmethod
	def create_random_eulerian(n):
		if n < 2:
			return None
		arr = [random.randrange(0, n+2, 2) for i in range(n)]
		while not Algorithms.is_degree_seq(arr):
			arr = [random.randrange(0, n+2, 2) for i in range(n)]
		graph = Algorithms.degree_seq_to_graph(arr)

		return graph

	@staticmethod
	def max_connected_comp(graph: Graph):
		def deep_first_search(adj_list, temp, vertex, visited):
			# Zaznaczamy aktualny jako odwiedzony i dodajemy go do listy
			visited[vertex] = True
			temp.append(vertex)
			for el in adj_list.list[vertex]:
				if not visited[el.id]:
					temp = deep_first_search(adj_list, temp, el.id, visited)
			return temp

		adj_list = AdjacencyList(graph)

		visited = [False for el in adj_list.list.keys()]
		connected_comp = []
		for i in range(len(adj_list.list.keys())):
			if not visited[i]:
				start_vertex = i
				tmp = []
				connected_comp.append(deep_first_search(adj_list, tmp, start_vertex, visited))
		return connected_comp

