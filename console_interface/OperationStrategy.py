from copy import copy

from .errors import *

from .readers import adjacency_matrix, incidence_matrix, adjacency_list, plain, cost_matrix
from .printers import console_printer, file_printer, image_printer


readers_map = {
    '--am': adjacency_matrix,
    '--cm': cost_matrix,
    '--im': incidence_matrix,
    '--al': adjacency_list,
    '--plain': plain
}

output_targets = {
    '--file': file_printer,
    '-f': file_printer,
    '--console': console_printer,
    '-c': console_printer,
    '--image': image_printer,
    '-i': image_printer
}


class OperationStrategy:
    """
    Instance of this class represents single operation in console interface (single task from given project,
    eg. graph randomization, hamiltonian cycle finding etc.) with included arguments validation for specific operation.
    """
    def __init__(self, name, resolver, description='Operation description...', ins=None, outs=None):
        self.name = name
        self.resolver = resolver
        self.description = description
        self.supported_sources = ins if ins is not None else {}
        self.supported_destinations = outs if outs is not None else {}

    def run(self, src, in_args, dest, out_args, resolver_args):
        self.validate_args(src, in_args, dest, out_args)
        data = None

        if src == '--file' or src == '-f':
            filename = in_args[0]
            reader = readers_map[in_args[1]]
            data = reader(filename)
        elif (src == '--console' or src == '-c') and in_args[0] == '--gseq':
            sequence = input('Enter number sequence:\n')
            data = [int(number) for number in sequence.split(' ')]

        result = self.resolver(data, resolver_args)

        printer = output_targets[dest]
        filename = ""

        if dest == '--file' or dest == '-f':
            filename = out_args[0]

        printer(result, filename)

    def validate_args(self, src, in_args, dest, out_args):
        if src not in self.supported_sources.keys():
            raise UnsupportedDataSource('Provided data source is not supported for this operation')

        if dest not in self.supported_destinations.keys():
            raise UnsupportedOutputTarget('Provided data output target is not supported for this operation')

        if src == '--file' or src == '-f':
            if len(in_args) != 2:
                raise MissingSourceArguments('Missing arguments for file data source (must be filename and data type)')
            else:
                src_file = in_args[0]
                input_data_type = in_args[1]

                if input_data_type not in self.supported_sources[src]:
                    raise UnsupportedDataType('This data type is not supported for this operation')

        if src == '--console' or src == '-c':
            if len(in_args) != 1:
                raise MissingSourceArguments('Missing input type for console data source')
            else:
                input_data_type = in_args[0]

                if input_data_type not in self.supported_sources[src]:
                    raise UnsupportedDataType('This data type is not supported for console data source')

        if dest == '--file' or dest == '-f':
            if len(out_args) < 1:
                raise MissingDestinationArguments('Missing output filename')


def build_options(options_tuples_list):
    options = dict()

    for (srcs_dests, data_types) in options_tuples_list:
        for src_dest in srcs_dests:
            options[src_dest] = copy(data_types)

    return options
