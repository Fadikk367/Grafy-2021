def console_printer(result, _):
    print()
    print(result)


def file_printer(result, filename="data/out.txt"):
    with open(filename, 'w') as f:
        f.write(str(result))


def image_printer(result, _):
    print('image printer')
