from .Graph import *

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
		return Graph(nodes, edges)



