class InputException(Exception):
    """A general exception to indicate that the input session
    file is malformed.
    """
    pass


class MissingInputKey(InputException):
    """A required key is missing from the input session file.
    """
    pass



