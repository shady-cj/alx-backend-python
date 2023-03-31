#!/usr/bin/env python3
"""
annotating functions
"""
from typing import Union, Sequence, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    duck typing by accept any object that can be indexed
    """
    if lst:
        return lst[0]
    else:
        return None
