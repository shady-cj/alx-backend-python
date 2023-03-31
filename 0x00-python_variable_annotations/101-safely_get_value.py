#!/usr/bin/env python3
"""
annotating functions
"""
from typing import Union, Mapping, Any, TypeVar
T = TypeVar("T")


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """
    duck typing by accept a dict and a key to access it
    """
    if key in dct:
        return dct[key]
    else:
        return default
