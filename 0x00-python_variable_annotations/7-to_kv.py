#!/usr/bin/env python3

"""
Module defines function to_kv
"""


from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    returns tuple with 1st element k and 2nd element square of v
    """
    return (k, v * v)
