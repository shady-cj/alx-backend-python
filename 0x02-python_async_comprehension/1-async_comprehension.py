#!/usr/bin/env python3
"""
This module contains a function named async_comprehension
that take no args and returns the list comprehension of values
from an async generator
"""
from typing import List
async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """
    The function returns a list comprehension from async generator
    """
    return [val async for val in async_generator()]
