from __future__ import absolute_import, print_function, unicode_literals


def guard(func, against=None):
    """
    Method to guard against exception or list of exceptions on method proveded.
    If `against` is None, it guards against all exceptions.

    Args:
        func(function): function to guard against
        against: Exception class or tuple of Exception classes

    Returns (function): Executes method

    Raises: Raises exceptions provided in :meth:`~transporter.utils.guard.guard` if caught.
    """
    try:
        return func()
    except Exception as e:
        if against and not isinstance(e, against):
            raise
    return None
