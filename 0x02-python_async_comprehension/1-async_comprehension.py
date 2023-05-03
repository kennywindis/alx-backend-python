#!/usr/bin/env python3
""" import async_generator from the previous task and write a coroutine that takes no args """
import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """ async Comprehensions """
    k = [i async for i in async_generator()]
    return k

