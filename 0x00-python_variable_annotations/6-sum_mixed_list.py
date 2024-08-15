#!/usr/bin/env python3

"""
Module defines  function mxd list
"""


from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """
    returns sum of mxd_list elements
    """
    return sum(mxd_list)
