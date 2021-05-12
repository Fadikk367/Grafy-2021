from .Graph import *
import random, copy


class Algorithms:

	@staticmethod
	def is_degree_seq(Arr):
		A = Arr.copy()
		if Algorithms.count_odds(A)%2 == 1:
			return False
		A.sort(reverse=True)
		flag = False
		while(True):
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
			if elem%2 == 1:
				count += 1
		return count


	@staticmethod
	def degree_seq_to_graph(Arr):
		A = Arr.copy()
		A.sort(reverse=True)
		if not Algorithms.is_degree_seq(A):
			return False
		nodes = [Node(i) for i in range(len(A))]
		edges = []
		for i in range(len(A)):
			for j in range(i+1, len(A)):
				if (A[i] > 0 and A[j] > 0):
					A[i] -= 1
					A[j] -= 1
					edges.append(Edge(nodes[i], nodes[j]))
		return Graph(edges, nodes)


	@staticmethod
	def pop_random_node(nodes):
		if len(nodes) > 0:
			node = random.choice(nodes)
			if node is not None:
				nodes.remove(node)
			return node


	@staticmethod
	def pick_random_node(nodes):
		node = random.choice(nodes)
		return node


	@staticmethod
	def check_node(node1, nodes, cycle):
		if node1 is None:
			return None
		try:
			node2 = random.choice(nodes)
		except IndexError:
			return None
		if (Edge(node1, node2) or Edge(node2, node1)) in cycle:
			return None
		if node2 is None:
			return None
		nodes.remove(node2)
		cycle.append(Edge(node1, node2))
		return node2


	@staticmethod
	def create_random_eulerian(n):
		connected_nodes = []
		unconnected_nodes = [Node(i) for i in range(n)]
		cycle = []
		node_degree = {}
		node1 = Algorithms.pop_random_node(unconnected_nodes)
		node2 = Algorithms.pop_random_node(unconnected_nodes)
		connected_nodes.append(node1)
		connected_nodes.append(node2)
		cycle.append(Edge(node1, node2))
		node_degree[node1] = 1
		node_degree[node2] = 1
		while len(unconnected_nodes) > 0:
			node1 = Algorithms.pick_random_node(connected_nodes)
			node2 = Algorithms.pop_random_node(unconnected_nodes)
			connected_nodes.append(node2)
			cycle.append(Edge(node1, node2))
			node_degree[node1] += 1
			node_degree[node2] = 1

		odd_nodes = [i for i, v in node_degree.items() if v % 2 == 1]
		even_nodes = [i for i, v in node_degree.items() if v % 2 == 0]
		while len(odd_nodes) > 0:
			node1 = Algorithms.pop_random_node(odd_nodes)
			if node1 is not None:
				node2 = Algorithms.check_node(node1, odd_nodes, cycle)
			if node2 is not None:
				even_nodes.append(node1)
				even_nodes.append(node2)
			else:
				node2 = Algorithms.check_node(node1, even_nodes, cycle)
				odd_nodes.append(node2)
				even_nodes.append(node1)

		return Graph(even_nodes, cycle)


	@staticmethod
	def create_random_eulerian2(n):
		if n < 2:
			return None
		arr = [random.randrange(0, n+2, 2) for i in range(n)]
		while not Algorithms.is_degree_seq(arr):
			arr = [random.randrange(0, n+2, 2) for i in range(n)]
			print(arr)
		graph = Algorithms.degree_seq_to_graph(arr)
		return graph

