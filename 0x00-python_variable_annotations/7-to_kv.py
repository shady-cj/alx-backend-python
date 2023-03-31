#!/usr/bin/env python3
"""
a module that contains a to_kv function
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    returns a tuple of k and v**2
    """
    return (str(k), v**2)
