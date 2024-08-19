#!/usr/bin/env python3

"""
Module defines a function that measures function runtime
"""

import asyncio
from typing import Callable
import time


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the average runtime of the wait_n function.

    Args:
        n (int): The number of times to call the wait_n function.
        max_delay (int): The maximum delay for each call to wait_n.

    Returns:
        float: The average runtime per call to wait_n.
    """
    wait_n: Callable = __import__('1-concurrent_coroutines').wait_n
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    return (end_time - start_time) / n
