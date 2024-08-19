#!/usr/bin/env python3

"""
Module defines function that spawns n tasks and waits for random delays
"""

import asyncio
from typing import List, Callable
wait_random: Callable = __import__('0-basic_async_syntax').wait_random
task_wait_random: Callable = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns n tasks that wait for a random delay and returns the list of delays.

    Args:
        n (int): The number of tasks to spawn.
        max_delay (int): The maximum delay for each task.

    Returns:
        List[float]: A sorted list of delays for each task.
    """
    tasks = []
    for _ in range(n):
        tasks.append((task_wait_random(max_delay)))
    # elapsed_times = [await task for task in tasks]
    elapsed_times = [await task for task in asyncio.as_completed(tasks)]
    return sorted(elapsed_times)
