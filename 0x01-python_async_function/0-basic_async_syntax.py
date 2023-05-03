#!/usr/bin/env python3
"""basic async func"""

import random
import asyncio

async def wait_random(max_delay: int = 10) -> float:
    """asynchronous coroutine that takes in an integer, wait for random delay and returns it"""
    k_float= k.uniform(0, max_delay)
    await asyncio.sleep(k_float)
    return k_float

