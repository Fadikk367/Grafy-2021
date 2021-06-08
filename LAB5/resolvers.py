from graphs.Graph import Graph
from graphs.Algorithms import Algorithms

import networkx as nx
import matplotlib.pyplot as plt

def generate_flow_network(data, _):
	N = int(data)
	if N <= 1:
		return "Network size should be greater than 1"

	network = Algorithms.generate_flow_network(N)
	Algorithms.ford_fulkerson(network, 0, N - 1)
	print("network: ", network)
	print("layers: ", network.layers)
	graph = nx.DiGraph()

	for i in range(len(network.layers)):
		for j in network.layers[i]:
			graph.add_node(j, subset=i)

	for edge in network.edges:
		nodes = edge.nodes
		print("edge capacity: ", edge.capacity, "edge flow: ", edge.flow)
		graph.add_edge(nodes[0].id, nodes[1].id, capacity = edge.capacity, flow = edge.flow)

	labels = {}
	for node in network.nodes:
		labels[node.id] = node.id



	edge_labels = dict([((u, v,), str(d['capacity'])) for u, v, d in graph.edges(data=True)])

	pos = nx.multipartite_layout(graph)
	nx.draw(graph, pos, labels=labels)
	nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels, label_pos=0.3)

	plt.axis("equal")
	plt.savefig("graph.png", format="png")
	plt.clf()
	ret = ''
	for edge in network.edges:
		ret += f'{edge.nodes[0]}-->{edge.nodes[1]} cap: {edge.capacity}\n'


	return ret


generate_flow_network(2, 5)