#!/usr/bin/env python3

"""
Module defines function element length
"""


from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    returns list of tuples of iterable and it's length
    """
    return [(i, len(i)) for i in lst]
