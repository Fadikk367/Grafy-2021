from console_interface.OperationStrategy import OperationStrategy, build_options
from console_interface.enums import DataSources, DataTypes, DataDestinations

from .resolvers import dijkstra_resolver, distance_matrix_resolver, center_resolver, random_weighted_graph_resolver, \
    kruskal_resolver


operations = [
    OperationStrategy(name='dijkstra',
                      resolver=dijkstra_resolver,
                      description='Builds a graph based on given sequence',
                      ins=build_options([(DataSources.FILE, DataTypes.COST_MATRIX)]),
                      outs=build_options([(DataDestinations.FILE, DataTypes.ADJ_MATRIX),
                                          (DataDestinations.CONSOLE, DataTypes.ADJ_MATRIX)])),
    OperationStrategy(name='distance_matrix',
                      resolver=distance_matrix_resolver,
                      description='Builds a graph based on given sequence',
                      ins=build_options([(DataSources.FILE, DataTypes.COST_MATRIX)]),
                      outs=build_options([(DataDestinations.FILE, DataTypes.ADJ_MATRIX),
                                          (DataDestinations.CONSOLE, DataTypes.ADJ_MATRIX)])),
    OperationStrategy(name='center',
                      resolver=center_resolver,
                      description='Builds a graph based on given sequence',
                      ins=build_options([(DataSources.FILE, DataTypes.COST_MATRIX)]),
                      outs=build_options([(DataDestinations.FILE, DataTypes.ADJ_MATRIX),
                                          (DataDestinations.CONSOLE, DataTypes.ADJ_MATRIX)])),
    OperationStrategy(name='random_connected_graph',
                      resolver=random_weighted_graph_resolver,
                      description='Generates random connected graph with given number of nodes',
                      ins=build_options([(DataSources.FILE, DataTypes.PLAIN)]),
                      outs=build_options([(DataDestinations.FILE, DataTypes.ADJ_MATRIX),
                                          (DataDestinations.CONSOLE, DataTypes.ADJ_MATRIX)])),
    OperationStrategy(name='kruskal',
                      resolver=kruskal_resolver,
                      description='Calculates minimal spanning tree using kruskal algorithm',
                      ins=build_options([(DataSources.FILE, DataTypes.COST_MATRIX)]),
                      outs=build_options([(DataDestinations.FILE, DataTypes.ADJ_MATRIX),
                                          (DataDestinations.CONSOLE, DataTypes.ADJ_MATRIX)])),
]
