from console_interface.ConsoleInterface import ConsoleInterface
from .operations import operations

# TODO If someone knows how to get it running (imports errors) from this nested directory feel free to fix it
if __name__ == "__main__":
    # Runs interface only for project 3 tasks
    CI = ConsoleInterface(operations)
    CI.start()
