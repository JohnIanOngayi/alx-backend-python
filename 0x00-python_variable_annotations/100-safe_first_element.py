#!/usr/bin/env python3

"""
Module defines function safe_first_element
"""


from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    returns 1st element if lst is iterable else None
    """
    if lst:
        return lst[0]
    else:
        return None
