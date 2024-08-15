#!/usr/bin/env python3

"""
Module defines function make_multiplier
"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    returns function that multiplies float by multiplier
    """
    return lambda x: x * multiplier
