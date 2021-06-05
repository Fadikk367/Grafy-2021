class DataTypes:
    ADJ_MATRIX = ['--am']
    DIRECTED_ADJ_MATRIX = ['--dam']
    COST_MATRIX = ['--cm']
    DIRECTED_COST_MATRIX = ['--dcm']
    PLAIN = ['--plain']
    ADJ_LIST = ['--al']
    INC_MATRIX = ['--im']
    ALL_MATRIXES = ['--am', '--im', '--al']
    SEQUENCE = ['--gseq']


class DataSources:
    FILE = ['--file', '-f']
    CONSOLE = ['--console', '-c']


class DataDestinations:
    FILE = ['--file', '-f']
    CONSOLE = ['--console', '-c']
    IMAGE = ['--image', '-i']