#!/usr/bin/env python3
"""basic async func"""

import random
import asyncio

async def wait_random(max_delay: int = 10) -> float:
    """asynchronous coroutine that takes in an integer, wait for random delay and returns it"""
    random_float = random.uniform(0, max_delay)
    await asyncio.sleep(random_flat)
    return random_float
