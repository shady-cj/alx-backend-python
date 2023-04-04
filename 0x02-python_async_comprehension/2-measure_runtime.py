#!/usr/bin/env python3
"""
This module contains a function that measures the
runtime of the 4 async_comprehension() function
run in parallel. It's observed that it runs at
roughly 10secs
"""
import time
import asyncio
async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """
    The function measures 4 async_comprehension()
    function runtime run in parallel.
    """
    tasks = []
    for i in range(4):
        tasks.append(async_comprehension())
    start = time.perf_counter()
    await asyncio.gather(*tasks)
    end = time.perf_counter()
    return end - start
