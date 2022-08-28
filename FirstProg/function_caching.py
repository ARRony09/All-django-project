import time
from functools import lru_cache


@lru_cache(maxsize=32)
def some_task(n):
    time.sleep(n)
    return n

if __name__ =='__main__':
    print("now running ")
    some_task(3)
    some_task(1)
    some_task(2)
    some_task(6)
    print("Done...\n")
    some_task(3)
    print("calling again")