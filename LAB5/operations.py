from console_interface.OperationStrategy import OperationStrategy, build_options
from console_interface.enums import DataSources, DataTypes, DataDestinations

from .resolvers import generate_flow_network


operations = [
    OperationStrategy(name='generate_network',
                      resolver=generate_flow_network,
                      description='Generates random flow network with given number of layers and runs Ford-Fulkerson algorithm',
                      ins=build_options([(DataSources.FILE, DataTypes.PLAIN)]),
                      outs=build_options([(DataDestinations.CONSOLE, DataTypes.PLAIN)])),
]