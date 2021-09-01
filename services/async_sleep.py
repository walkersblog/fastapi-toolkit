import asyncio
import time


async def async_sleep(start, seconds):
    print(f'Time: {time.time() - start:.2f}')
    await asyncio.sleep(seconds)
    interval = time.time() - start
    return interval
