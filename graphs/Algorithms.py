from .Graph import Graph, AdjacencyList, Node, Edge
from queue import PriorityQueue

import random, copy
import math
from collections import defaultdict


class Algorithms:
	"""
	This static methods class gathers algorithms from all projects
	"""
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
	def hamiltonian_cycle(graph: Graph, v=None, cycle=None):
		adjacency_list = AdjacencyList(graph)
		nodes = adjacency_list.get_nodes()

		if cycle is None:
			cycle = []
		if v is None:
			v = nodes[0]

		if v not in set(cycle):
			cycle.append(v)

			if len(cycle) == len(nodes):  # we have a hamilton's path
				closing_edge = Edge(Node(cycle[0]), Node(cycle[-1]))

				if graph.has_edge(closing_edge):  # check if there is a connection between last node in path and the first one
					cycle.append(cycle[0])
					# if so, we have cycle then
					return cycle
				else:
					cycle.pop()
					return None
			else:
				for neighbour in adjacency_list.get_neighbours(v):
					cycle_copy = cycle[:]
					hamiltonian_candidate = Algorithms.hamiltonian_cycle(graph, neighbour, cycle_copy)
					if hamiltonian_candidate is not None:
						return hamiltonian_candidate

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

	@staticmethod
	def generate_random_regular_graph(k, n, seed=random):
		"""
		returns k-regular graph with n vertices -> as adjacency matrix
		k * n must be even number

		:param k: graph degree
		:param n: number of vertices
		"""

		# takes list of edges and number of nodes, returns adjacency matrix
		def adjacency_matrix_from_edges_set(edges_set, n):
			rows, cols = (n, n)
			arr = []
			for i in range(rows):
				col = []
				for j in range(cols):
					col.append(0)
				arr.append(col)
			for edge in edges_set:
				arr[edge[0]][edge[1]] = 1
				arr[edge[1]][edge[0]] = 1
			return arr

		# make sure that none of the vertices have loops or multiple edges
		def is_plain(edges, potential_edges):

			if not potential_edges:
				return True

			for point1 in potential_edges:
				for point2 in potential_edges:
					if point1 == point2:
						break
					if point1 > point2:
						point1, point2 = point2, point1
					if (point1, point2) not in edges:
						return True

			return False

		def generate():

			edges_set = set()
			buckets = list(range(n)) * k

			while buckets:
				# takes zero when argument is not present potential_edges[argument] -> potential_edges[argument] = 0
				potential_edges = defaultdict(int)
				seed.shuffle(buckets)
				bucket_iterator = iter(buckets)

				# we match randomly 2 points from buckets in order to retrieve edges
				for point1, point2 in zip(bucket_iterator, bucket_iterator):
					# replace if needed, first number need be smaller
					if point1 > point2:
						point1, point2 = point2, point1
					# if not already in edges set we put it and send further for testing
					if point1 != point2 and ((point1, point2) not in edges_set):
						edges_set.add((point1, point2))
					# if such edge exists we increment possible edge from this node
					else:
						potential_edges[point1] += 1
						potential_edges[point2] += 1

				# check if set fulfills expectations
				if not is_plain(edges_set, potential_edges):
					return None

				# refreshing bucket with nodes repeated * their potential
				buckets = [node for node, potential in potential_edges.items() for _ in range(potential)]

			return edges_set

		if (n * k) % 2 != 0:
			raise ValueError("n * k must be even")

		if not 0 <= k < n:
			raise ValueError("the 0 <= d < n inequality must be satisfied")

		if k == 0:
			return adjacency_matrix_from_edges_set({}, n)

		# first shot
		result = generate()

		# retry graph generation when previous one fell short of expectations
		# if the graph is not simple -> restart
		while result is None:
			result = generate()

		return adjacency_matrix_from_edges_set(result, n)

	@staticmethod
	def dijkstra(graph: Graph, start_node):
		# init
		d_s = [math.inf for node in graph.nodes]
		p_s = [None for node in graph.nodes]
		d_s[start_node] = 0

		unvisited_nodes = PriorityQueue()
		for i, v in enumerate(d_s):
			unvisited_nodes.put((v, i))

		while not unvisited_nodes.empty():
			distance, node_id = unvisited_nodes.get()
			# print(f"dist: {distance}, node_id: {node_id}")
			neighbours = graph.get_neighbours(node_id)
			# print(f"neighbours: {neighbours}")
			for neighbour in neighbours:
				edge = graph.get_edge_with_nodes(node_id, neighbour.id)
				# print(f"edge: {edge}")

				if d_s[neighbour.id] > d_s[node_id] + edge.weight:
					d_s[neighbour.id] = d_s[node_id] + edge.weight
					p_s[neighbour.id] = node_id

					updated_unvisited_nodes = PriorityQueue()
					for v, i in unvisited_nodes.queue:
						if i == neighbour.id:
							v = d_s[node_id] + edge.weight
						updated_unvisited_nodes.put((v, i))
					unvisited_nodes = updated_unvisited_nodes

		# print(f"start: {start_node}")
		# print(d_s)
		# print(p_s)
		# for node, distance in enumerate(d_s):
		# 	prev = p_s[node]
		# 	path = [str(node)]
		#
		# 	while prev is not None:
		# 		path.append(str(prev))
		# 		prev = p_s[prev]
		#
		# 	path.reverse()
		# 	print(f"d({node}) = {distance}, path: [{' - '.join(path)}]")

		return start_node, d_s, p_s

	@staticmethod
	def distance_matrix(graph: Graph):
		matrix = []

		for i, node in enumerate(graph.nodes):
			_1, d_s, _2 = Algorithms.dijkstra(graph, i)
			matrix.append(d_s)

		# print(matrix)
		return matrix

	@staticmethod
	def graph_center(graph: Graph):
		distance_matrix = Algorithms.distance_matrix(graph)
		row_sums = [sum(row) for row in distance_matrix]
		min_row_sum = min(row_sums)
		center_node_id = row_sums.index(min_row_sum)

		return center_node_id

	@staticmethod
	def graph_minimax_center(graph: Graph):
		distance_matrix = Algorithms.distance_matrix(graph)
		row_maxes = [max(row) for row in distance_matrix]
		minimax_distance = min(row_maxes)
		minimax_node_id = row_maxes.index(minimax_distance)

		return minimax_node_id
