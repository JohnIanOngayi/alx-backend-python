#!/usr/bin/env python3

"""
Module defines function that waits n times with specific max delay time
"""

import asyncio
from typing import List, Callable
wait_random: Callable = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns wait_random n times with the specified max_delay.

    Args:
        n (int): The number of times to spawn wait_random.
        max_delay (int): The maximum delay for wait_random.

    Returns:
        List[float]: A list of elapsed times for each wait_random call,
                        sorted in ascending order.
    """
    tasks = []
    for _ in range(n):
        tasks.append(asyncio.create_task(wait_random(max_delay)))
    elapsed_times = [await task for task in asyncio.as_completed(tasks)]
    return sorted(elapsed_times)
