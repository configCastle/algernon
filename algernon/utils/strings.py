"""Functions for string."""


def str_to_bool(string):
    """
    Transform 'True' to True, 'False' to False.

    Args:
        string: 'False' or 'True'

    Returns:
        False or True
    """
    if string == 'True':
        return True
    elif string == 'False':
        return False
