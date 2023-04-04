#!/usr/bin/env python3
"""
This module contains a function named async_generator
that creates and  async generator.
"""
import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    The function yields a random number between 0 and 10
    while waiting for 1 sec during iterations.
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
