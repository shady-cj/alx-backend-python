#!/usr/bin/python3
"""
a module that contains a type annotated
make_multiplier function
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    returns a function that multiplies multiplier
    by a float arg
    """
    return lambda x: x * multiplier
