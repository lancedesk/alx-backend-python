#!/usr/bin/env python3
"""
Asynchronous coroutine that yields random numbers after waiting asynchronously.
"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Asynchronous coroutine that yields a random number between 0 and 10
    after waiting for 1 second asynchronously, repeated 10 times.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
