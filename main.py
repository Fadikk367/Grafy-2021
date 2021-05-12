from console_interface.ConsoleInterface import ConsoleInterface
from console_interface.OperationStrategy import OperationStrategy, build_options
from console_interface.enums import DataTypes, DataSources, DataDestinations

from LAB2.zad6 import hamilton_cycle_resolver, randomization_resolver, max_connected_comp_resolver


if __name__ == "__main__":
    operations = [
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
        OperationStrategy('hamiltonian_cycle',
                          hamilton_cycle_resolver,
                          'Finds a hamiltonian cycle on a graph',
                          build_options([(DataSources.FILE, DataTypes.ALL_MATRIXES), (DataSources.CONSOLE, DataTypes.SEQUENCE)]),
                          build_options([(DataDestinations.FILE, DataTypes.ADJ_MATRIX), (DataDestinations.CONSOLE, DataTypes.ADJ_MATRIX)])),
    ]

    CI = ConsoleInterface(operations)

    CI.start()
