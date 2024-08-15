#!/usr/bin/env python3

"""
Module defines function safely_get_value
"""

from typing import Any, Mapping, TypeVar, Union


T = TypeVar("T")


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """
    safely returns value to key from dct
    """
    if key in dct:
        return dct[key]
    else:
        return default
