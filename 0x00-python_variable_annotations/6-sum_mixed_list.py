#!/usr/bin/env python3
"""
a module that contains a sum_mixed_list function
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    returns the sum of mxd_list of ints
    and floats as a float
    """
    return sum(mxd_lst)
