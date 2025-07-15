from __future__ import absolute_import, print_function, unicode_literals
import re

import six


PATH_DELIMITERS = [".", ",", "[", "]"]
YES = ["YES", "TRUE", "1"]


def _split_and_trim(string, *delimiters):
    pattern = "|".join(map(re.escape, delimiters))
    return filter(None, re.split(pattern, string, 0))


def _parse_path(path):
    if isinstance(path, six.string_types):
        path = _split_and_trim(path, *PATH_DELIMITERS)

    for key in path:
        if isinstance(key, six.string_types):
            for k in _split_and_trim(key, *PATH_DELIMITERS):
                yield k
        else:
            yield key


def getpath(obj, path, default=None):
    """Gets the value following the path list, if the path doesn't exitst
    returns the default value

    Args:
        obj(dict): list or dict to examine
        path(list|str): list of keys to follow to examine

    Returns:
        value located in the path location

    Example:

        .. code-block:: bash

            $ python


        .. code-block:: python

            from audicus.utils.get_path import getpath

            getpath({'one': {'two': {'three': 4}}}, ['one', 'two'])
            {'three': 4})

            getpath({'one': {'two': {'three': 4}}}, 'one.two')
            {'three': 4})

            getpath({'one': {'two': {'three': 4}}}, ['one', 'four'])
            None

            getpath({'one': {'two': {'three': 4}}}, 'one.four')
            None

            getpath({'one': ['two', {'three': [4, 5]}]}, ['one', 1, 'three'])
            [4, 5]

            getpath(['one', {'two': {'three': [4, 5]}}], '[1].two.three.[0]')
            4

            getpath({'one': ['two', {'three': [4, 5]}]}, 'one[1].three')
            [4, 5]

            getpath([range(50)], [0, 42])
            42

            getpath([[[[[[[[[[42]]]]]]]]]], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
            42
    """
    for key in _parse_path(path):
        try:
            try:
                obj = obj[key]
            except TypeError:
                obj = obj[int(key)]
        except (KeyError, IndexError, TypeError, AttributeError, ValueError):
            obj = default

        if obj is None:
            break
    return obj
