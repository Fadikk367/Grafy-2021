from .errors import Error, TooFewArguments


class ConsoleInterface:
    """
    Class for handling user interaction with program through system console
    """
    def __init__(self, operations_list):
        operations = {operation.name: operation for operation in operations_list}
        default_operations = {
            'help': self.print_operations,
            'exit': self.exit
        }
        self.terminate = False
        self.operations = {**operations, **default_operations}

    def print_operations(self, args=None):
        print('Available operations:')
        for name, operation in self.operations.items():
            if name != 'exit' and name != 'help':
                print(f'- {name} => {operation.description}')

        print(f'- help => prints supported operations')
        print(f'- exit => quits the program')

    def exit(self, args=None):
        self.terminate = True

    def start(self):
        while True:
            try:
                user_input = input('$ ')
                self.handle_command(user_input)

                if self.terminate:
                    print('Terminating program...')
                    break

            except ValueError as e:
                print('Invalid command structure!')
                print('Should be:')
                print('<command> --<data_source> --<input_type> --out --<output_target>')
            except KeyError:
                print('Invalid or unsupported command!')
            except IOError:
                print('No such file or directory')
            except Error as err:
                print(err.message)

    def handle_command(self, command):
        if command == 'exit':
            self.exit()
            return
        elif command == 'help':
            self.print_operations()
            return
        else:
            tokens = command.split(' ')
            if len(tokens) < 5:
                raise TooFewArguments('Too few arguments provided!')

            operation = tokens[0]
            in_index = tokens.index('--in')
            out_index = tokens.index('--out')

            resolver_args = tokens[1: in_index]
            inp_args = tokens[in_index + 1:out_index]
            out_args = tokens[out_index + 1:]

            src_type = inp_args.pop(0)
            dest_type = out_args.pop(0)

            strategy = self.operations[operation]

            strategy.run(src_type, inp_args, dest_type, out_args, resolver_args)
