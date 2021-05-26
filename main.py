from console_interface.ConsoleInterface import ConsoleInterface
from console_interface.OperationStrategy import OperationStrategy, build_options
from console_interface.enums import DataTypes, DataSources, DataDestinations

from LAB2.zad6 import hamilton_cycle_resolver, randomization_resolver, max_connected_comp_resolver, \
    create_random_eulerian_resolver, sequence_to_graph_resolver, k_regular_graph_resolver

from LAB3.resolvers import random_weighted_graph_resolver, dijkstra_resolver, distance_matrix_resolver, center_resolver, kruskal_resolver


if __name__ == "__main__":
    operations = [
        OperationStrategy('sequence',
                          sequence_to_graph_resolver,
                          'Builds a graph based on given sequence',
                          build_options(
                              [(DataSources.CONSOLE, DataTypes.SEQUENCE)]),
                          build_options([(DataDestinations.FILE, DataTypes.ADJ_MATRIX),
                                         (DataDestinations.CONSOLE, DataTypes.ADJ_MATRIX)])),
        OperationStrategy('randomize',
                          randomization_resolver,
                          'Finds a hamiltonian cycle on a graph',
                          build_options(
                              [(DataSources.FILE, DataTypes.ALL_MATRIXES), (DataSources.CONSOLE, DataTypes.SEQUENCE)]),
                          build_options([(DataDestinations.FILE, DataTypes.ADJ_MATRIX),
                                         (DataDestinations.CONSOLE, DataTypes.ADJ_MATRIX)])),
        OperationStrategy('components',
                          max_connected_comp_resolver,
                          'Finds all components on a graph',
                          build_options(
                              [(DataSources.FILE, DataTypes.ADJ_MATRIX)]),
                          build_options([(DataDestinations.FILE, DataTypes.ADJ_MATRIX),
                                         (DataDestinations.CONSOLE, DataTypes.ADJ_MATRIX)])),
        OperationStrategy('euler',
                          create_random_eulerian_resolver,
                          'Generates eulerian graph with given number of nodes',
                          build_options(
                              [(DataSources.FILE, DataTypes.PLAIN)]),
                          build_options([(DataDestinations.FILE, DataTypes.ADJ_MATRIX),
                                         (DataDestinations.CONSOLE, DataTypes.ADJ_MATRIX)])),
        OperationStrategy('k_regular',
                          k_regular_graph_resolver,
                          'Generates k regular graph with n nodes',
                          build_options(
                              [(DataSources.FILE, DataTypes.PLAIN)]),
                          build_options([(DataDestinations.FILE, DataTypes.ADJ_MATRIX),
                                         (DataDestinations.CONSOLE, DataTypes.ADJ_MATRIX)])),
        OperationStrategy('hamilton',
                          hamilton_cycle_resolver,
                          'Finds a hamiltonian cycle on a graph',
                          build_options([(DataSources.FILE, DataTypes.ADJ_MATRIX), (DataSources.CONSOLE, DataTypes.SEQUENCE)]),
                          build_options([(DataDestinations.FILE, DataTypes.ADJ_MATRIX), (DataDestinations.CONSOLE, DataTypes.ADJ_MATRIX)])),
        OperationStrategy('dijkstra',
                          dijkstra_resolver,
                          'Builds a graph based on given sequence',
                          build_options(
                              [(DataSources.FILE, DataTypes.COST_MATRIX)]),
                          build_options([(DataDestinations.FILE, DataTypes.ADJ_MATRIX),
                                         (DataDestinations.CONSOLE, DataTypes.ADJ_MATRIX)])),
        OperationStrategy('distance_matrix',
                          distance_matrix_resolver,
                          'Builds a graph based on given sequence',
                          build_options(
                              [(DataSources.FILE, DataTypes.COST_MATRIX)]),
                          build_options([(DataDestinations.FILE, DataTypes.ADJ_MATRIX),
                                         (DataDestinations.CONSOLE, DataTypes.ADJ_MATRIX)])),
        OperationStrategy('center',
                          center_resolver,
                          'Builds a graph based on given sequence',
                          build_options(
                              [(DataSources.FILE, DataTypes.COST_MATRIX)]),
                          build_options([(DataDestinations.FILE, DataTypes.ADJ_MATRIX),
                                         (DataDestinations.CONSOLE, DataTypes.ADJ_MATRIX)])),
        OperationStrategy('random_connected_graph',
                          random_weighted_graph_resolver,
                          'Generates random connected graph with given number of nodes',
                          build_options(
                              [(DataSources.FILE, DataTypes.PLAIN)]),
                          build_options([(DataDestinations.FILE, DataTypes.ADJ_MATRIX),
                                         (DataDestinations.CONSOLE, DataTypes.ADJ_MATRIX)])),
        OperationStrategy('kruskal',
                          kruskal_resolver,
                          'Calculates minimal spanning tree using kruskal algorithm',
                          build_options(
                              [(DataSources.FILE, DataTypes.COST_MATRIX)]),
                          build_options([(DataDestinations.FILE, DataTypes.ADJ_MATRIX),
                                         (DataDestinations.CONSOLE, DataTypes.ADJ_MATRIX)])),
    ]

    CI = ConsoleInterface(operations)

    CI.start()
