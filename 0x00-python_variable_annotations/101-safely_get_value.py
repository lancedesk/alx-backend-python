#!/usr/bin/env python3
"""
Safely get value function
"""

from typing import Mapping, Any, TypeVar, Union

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None) -> Union[Any, T]:
    """
    Return the value associated with key in dct if it exists, otherwise return default
    """
    if key in dct:
        return dct[key]
    else:
        return default
