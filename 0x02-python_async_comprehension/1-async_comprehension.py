#!/usr/bin/env python3
"""
Asynchronous coroutine that collects 10 random numbers
using async comprehension.
"""

import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Asynchronous coroutine that collects 10 random numbers
    using async comprehension over async_generator.

    Returns:
        list[float]: List of 10 random numbers.
    """
    return [num async for num in async_generator()]
