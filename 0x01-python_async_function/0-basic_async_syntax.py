#!/usr/bin/env python3

"""
Module utilises asyncio to run coroutines
"""

import time
import asyncio
import random
from typing import Union


async def wait_random(max_delay: int = 10) -> Union[float, int]:
    """
    Asynchronous coroutine that waits for a random delay between 0 n max_delay

    Args:
        max_delay (int): The maximum delay in seconds. Default is 10 seconds.

    Returns:
        Union[float, int]: The actual time waited in seconds.
    """
    wait_time: int = random.randint(0, max_delay)
    start_time: float = time.time()
    await asyncio.sleep(wait_time)
    end_time: float = time.time()
    return end_time - start_time
