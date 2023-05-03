#!/usr/bin/env python3
"""measure runtime"""
import time
import asyncio

def measure_time(n: int, max_delay: int) -> float:
    """measures total execution time"""

wait_n = __import__('1-concurrent_coroutines').wait_n

start = time()
asyncio.run(wait_n(n, max_delay))
end = time()

    return (end - start) / n
