#!/usr/bin/env python3

"""
Module defines function that creates an asyncio task
"""

import asyncio
from typing import Callable
wait_random: Callable = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates an asyncio Task that waits for a random delay.

    Args:
        max_delay (int): The maximum delay in seconds.

    Returns:
        asyncio.Task: The created asyncio Task.
    """
    task: asyncio.Task = asyncio.create_task(wait_random(max_delay))
    return task
