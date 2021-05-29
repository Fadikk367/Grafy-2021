from console_interface.ConsoleInterface import ConsoleInterface

from LAB2.operations import operations as lab2_operations
from LAB3.operations import operations as lab3_operations
from LAB4.operations import operations as lab4_operations


if __name__ == "__main__":
    operations = [
        *lab2_operations,
        *lab3_operations,
        *lab4_operations,
    ]

    CI = ConsoleInterface(operations)

    CI.start()
