#!/usr/bin/env python3
"""
Asynchronous coroutine that yields random numbers after waiting asynchronously.
"""

import asyncio
import random


async def async_generator():
    """
    Asynchronous coroutine that yields a random number between 0 and 10
    after waiting for 1 second asynchronously, repeated 10 times.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
