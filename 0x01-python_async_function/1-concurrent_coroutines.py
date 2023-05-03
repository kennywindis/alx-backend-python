#!/usr/bin/env python3

"""Let's execute multiple coroutines at the same time with async"""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n: int, max_delay: int) -> List[float]:
    """ Let's execute multiple coroutines at the same time with async  """

k_list = [wait_random(max_delay) for i in range(n)]
completed_tasks = []

for task  in asyncio.as_completed(k_list):
    completed_tasks.append(await task)
    return completed_tasks
