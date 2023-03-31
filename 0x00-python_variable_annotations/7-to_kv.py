#!/usr/bin/env python3
"""
a module that contains a to_kv function
"""


def to_kv(k: str, v: int | float) -> tuple[str, float]:
    """
    returns a tuple of k and v**2
    """
    return (str(k), v**2)
