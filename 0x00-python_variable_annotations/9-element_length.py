#!/usr/bin/env python3
"""
annotating functions
"""
from typing import Iterable, List, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    duck typing by accept any list like iterable
    """
    return [(i, len(i)) for i in lst]
