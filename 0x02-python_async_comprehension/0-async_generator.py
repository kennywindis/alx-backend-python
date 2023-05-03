#!/usr/bin/env python3

""" async generator """

import asyncio
from typing import Generator
import random

async def async_generator() -> Generator[float, None, None]:
    """ a coroutine with no args """
    for k in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
