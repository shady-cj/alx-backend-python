#!/usr/bin/env python3
"""
Re-Implementing the wait_n function from 1-concurrent_coroutines.py
to call task_wait_random from 3-tasks.py
"""
from typing import List
import asyncio
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Implemented wait_n that returns a list of delays returned from
    task_wait_random and the sorting the list_of_delays list using the famous
    bubble sort.
    """
    list_of_delay_tasks = []
    for i in range(n):
        delay = task_wait_random(max_delay)
        list_of_delay_tasks.append(delay)

    list_of_delays = await asyncio.gather(*list_of_delay_tasks)
    for j in range(len(list_of_delays)):
        for k in range(j, len(list_of_delays)):
            if list_of_delays[j] > list_of_delays[k]:
                list_of_delays[j], list_of_delays[k] = \
                    list_of_delays[k], list_of_delays[j]
    return list_of_delays
