#!/usr/bin/env python3
"""
contains a function task_wait_random that returns an asyncio
Task
"""
import asyncio
wait_random = __import__("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    The function returns an asyncio task instance
    """
    return asyncio.create_task(wait_random(max_delay))
