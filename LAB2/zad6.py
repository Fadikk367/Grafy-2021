from grahps.Graph import Graph, AdjacencyMatrix
from grahps.Algorithms import Algorithms


def hamilton_cycle_resolver(graph: Graph, args):
    result = Graph.hamiltonian_cycle(graph)

    if result is None:
        return 'Given graph does not have an hamiltonian cycle'
    else:
        return result


def randomization_resolver(graph: Graph, args):
    permutations = int(args[0])

    graph.randomize(permutations)
    return AdjacencyMatrix(graph)


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


