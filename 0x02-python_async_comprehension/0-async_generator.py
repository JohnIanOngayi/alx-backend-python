#!/usr/bin/python3

"""
Module defines coroutine looping 10 times yielding a random no between 1 and 10
"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    An asynchronous generator that yields a random number between 1 and 10.

    This function will run a loop 10 times, and in each iteration, it will:
    1. Await for 1 second using asyncio.sleep(1).
    2. Yield a random floating-point number between 1 and 10.

    Yields:
        float: A random floating-point number between 1 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield (random.uniform(1, 10))
