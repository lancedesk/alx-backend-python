#!/usr/bin/env python3
"""
Measuring the total runtime of executing async_comprehension
multiple times in parallel.
"""

import asyncio
from typing import List
from time import perf_counter

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Coroutine that executes async_comprehension four times in parallel
    using asyncio.gather and measures the total runtime.

    Returns:
        float: Total runtime in seconds.
    """

    start_time = perf_counter()
    run_time = [asyncio.create_task(async_comprehension()) for _ in range(4)]
    await asyncio.gather(*run_time)
    total_runtime = perf_counter() - start_time
    return total_runtime
