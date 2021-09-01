import time


def sync_sleep(start, seconds):
    print(f'Time: {time.time() - start:.2f}')
    time.sleep(1)
    interval = time.time() - start
    return interval
