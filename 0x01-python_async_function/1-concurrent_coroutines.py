#!/usr/bin/env python3
"""
A module that implements the async function wait_n and import the async function
wait_random
"""
from typing import List
wait_random = __import__("0-basic_async_syntax").wait_random



async def wait_n(n: int, max_delay: int) -> List[float]:
    list_of_delays = []
    for i in range(n):
        delay = await wait_random(max_delay)
        list_of_delays.append(delay)
    for j in range(len(list_of_delays)):
        for k in range(j, len(list_of_delays)):
            if list_of_delays[j] > list_of_delays[k]:
                list_of_delays[j], list_of_delays[k] = list_of_delays[k], list_of_delays[j]
    return list_of_delays