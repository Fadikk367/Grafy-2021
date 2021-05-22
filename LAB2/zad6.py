from graphs.Graph import Graph, AdjacencyMatrix, AdjacencyList, Node
from graphs.Algorithms import Algorithms


def hamilton_cycle_resolver(graph: Graph, args):
    result = Algorithms.hamiltonian_cycle(graph)

    if result is None:
        return 'Given graph does not have an hamiltonian cycle'
    else:
        return result


def randomization_resolver(graph: Graph, args):
    permutations = int(args[0])
    try:
        graph.randomize(permutations)
        return AdjacencyMatrix(graph)
    except Exception:
        return 'Graph cannot be randomized'


def max_connected_comp_resolver(graph: Graph, args):
    components = Algorithms.max_connected_comp(graph)

    result = ""
    max_component_index = 0
    for i, component in enumerate(components):
        result += f"{i}) {component}\n"
        if len(component) == max([len(comp) for comp in components]):
            max_component_index = i

    result += f"Largest component have an index of {max_component_index}\n"
    return result


def create_random_eulerian_resolver(data, _):
    nodes = int(data)

    eulerian_graph = Algorithms.create_random_eulerian(nodes)
    euler_cycle = AdjacencyList.find_euler_path(AdjacencyList(eulerian_graph), Node(0))
    return euler_cycle


def sequence_to_graph_resolver(sequence, _):
    graph = Algorithms.degree_seq_to_graph(sequence)

    if graph is None:
        return "Given sequence does not represent a valid graph"

    return AdjacencyMatrix(graph)


def k_regular_graph_resolver(args, _):

    [nodes, degree] = [int(num) for num in args.split(' ')]

    result = Algorithms.generate_random_regular_graph(degree, nodes)
    graph = Graph()
    adj_matrix = AdjacencyMatrix(graph)
    adj_matrix.matrix = result

    return adj_matrix

