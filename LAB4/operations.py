from console_interface.OperationStrategy import OperationStrategy, build_options
from console_interface.enums import DataSources, DataTypes, DataDestinations

from .resolvers import random_digraph_resolver, kosaraju_resolver, random_strongly_connected_component_resolver, \
    bellman_ford_resolver, johnson_resolver


operations = [
    OperationStrategy(name='random_digraph',
                      resolver=random_digraph_resolver,
                      description='Generates random digraph with given number of nodes and edge probability',
                      ins=build_options([(DataSources.FILE, DataTypes.PLAIN)]),
                      outs=build_options([(DataDestinations.FILE, DataTypes.ADJ_MATRIX),
                                          (DataDestinations.CONSOLE, DataTypes.ADJ_MATRIX)])),
    OperationStrategy(name='kosaraju',
                      resolver=kosaraju_resolver,
                      description='Finds strong components on a digraph',
                      ins=build_options([(DataSources.FILE, DataTypes.DIRECTED_COST_MATRIX),
                                         (DataSources.FILE, DataTypes.DIRECTED_ADJ_MATRIX)]),
                      outs=build_options([(DataDestinations.FILE, DataTypes.ADJ_MATRIX),
                                          (DataDestinations.CONSOLE, DataTypes.ADJ_MATRIX)])),
    OperationStrategy(name='random_strongly_connected',
                      resolver=random_strongly_connected_component_resolver,
                      description='Generates random strongly connected graph',
                      ins=build_options([(DataSources.FILE, DataTypes.PLAIN)]),
                      outs=build_options([(DataDestinations.FILE, DataTypes.ADJ_MATRIX),
                                          (DataDestinations.CONSOLE, DataTypes.ADJ_MATRIX)])),
    OperationStrategy(name='bellman_ford',
                      resolver=bellman_ford_resolver,
                      description='Finds the shortest paths to other vertices',
                      ins=build_options([(DataSources.FILE, DataTypes.DIRECTED_COST_MATRIX)]),
                      outs=build_options([(DataDestinations.FILE, DataTypes.ADJ_MATRIX),
                                          (DataDestinations.CONSOLE, DataTypes.ADJ_MATRIX)])),
    OperationStrategy(name='johnson',
                      resolver=johnson_resolver,
                      description='Finds distances between all nodes for directed weighted graph',
                      ins=build_options([(DataSources.FILE, DataTypes.DIRECTED_COST_MATRIX)]),
                      outs=build_options([(DataDestinations.FILE, DataTypes.ADJ_MATRIX),
                                          (DataDestinations.CONSOLE, DataTypes.ADJ_MATRIX)])),
]