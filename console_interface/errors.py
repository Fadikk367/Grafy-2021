class Error(Exception):
    def __init__(self, message='Something went wrong!'):
        self.message = message


class TooFewArguments(Error):
    def __init__(self, message):
        super().__init__(message)


class UnsupportedOperationError(Error):
    def __init__(self, message):
        super().__init__(message)


class UnsupportedDataSource(Error):
    def __init__(self, message):
        super().__init__(message)


class UnsupportedDataType(Error):
    def __init__(self, message):
        super().__init__(message)


class MissingSourceArguments(Error):
    def __init__(self, message):
        super().__init__(message)


class MissingDestinationArguments(Error):
    def __init__(self, message):
        super().__init__(message)


class UnsupportedOutputTarget(Error):
    def __init__(self, message):
        super().__init__(message)
