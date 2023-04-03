#!/usr/bin/env python3
"""
A module that contains an async function wait_random
that waits for and returns a random number. between 0 and max_delay(inclusive)
"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> int:
    """
    The function waits and returns a random float between 0 and max_delay:
    inclusive.
    """
    n = random.uniform(0, max_delay)
    await asyncio.sleep(n)
    return n
