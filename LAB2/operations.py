from console_interface.OperationStrategy import OperationStrategy, build_options
from console_interface.enums import DataSources, DataTypes, DataDestinations

from .resolvers import sequence_to_graph_resolver, randomization_resolver, max_connected_comp_resolver, \
    create_random_eulerian_resolver, k_regular_graph_resolver, hamilton_cycle_resolver


operations = [
    OperationStrategy(name='sequence',
                      resolver=sequence_to_graph_resolver,
                      description='Builds a graph based on given sequence',
                      ins=build_options([(DataSources.CONSOLE, DataTypes.SEQUENCE)]),
                      outs=build_options([(DataDestinations.FILE, DataTypes.ADJ_MATRIX),
                                          (DataDestinations.CONSOLE, DataTypes.ADJ_MATRIX)])),
    OperationStrategy(name='randomize',
                      resolver=randomization_resolver,
                      description='Finds a hamiltonian cycle on a graph',
                      ins=build_options([(DataSources.FILE, DataTypes.ALL_MATRIXES),
                                         (DataSources.CONSOLE, DataTypes.SEQUENCE)]),
                      outs=build_options([(DataDestinations.FILE, DataTypes.ADJ_MATRIX),
                                          (DataDestinations.CONSOLE, DataTypes.ADJ_MATRIX)])),
    OperationStrategy(name='components',
                      resolver=max_connected_comp_resolver,
                      description='Finds all components on a graph',
                      ins=build_options([(DataSources.FILE, DataTypes.ADJ_MATRIX)]),
                      outs=build_options([(DataDestinations.FILE, DataTypes.ADJ_MATRIX),
                                          (DataDestinations.CONSOLE, DataTypes.ADJ_MATRIX)])),
    OperationStrategy(name='euler',
                      resolver=create_random_eulerian_resolver,
                      description='Generates eulerian graph with given number of nodes',
                      ins=build_options([(DataSources.FILE, DataTypes.PLAIN)]),
                      outs=build_options([(DataDestinations.FILE, DataTypes.ADJ_MATRIX),
                                          (DataDestinations.CONSOLE, DataTypes.ADJ_MATRIX)])),
    OperationStrategy(name='k_regular',
                      resolver=k_regular_graph_resolver,
                      description='Generates k regular graph with n nodes',
                      ins=build_options([(DataSources.FILE, DataTypes.PLAIN)]),
                      outs=build_options([(DataDestinations.FILE, DataTypes.ADJ_MATRIX),
                                          (DataDestinations.CONSOLE, DataTypes.ADJ_MATRIX)])),
    OperationStrategy(name='hamilton',
                      resolver=hamilton_cycle_resolver,
                      description='Finds a hamiltonian cycle on a graph',
                      ins=build_options([(DataSources.FILE, DataTypes.ADJ_MATRIX),
                                         (DataSources.CONSOLE, DataTypes.SEQUENCE)]),
                      outs=build_options([(DataDestinations.FILE, DataTypes.ADJ_MATRIX),
                                          (DataDestinations.CONSOLE, DataTypes.ADJ_MATRIX)])),
]
