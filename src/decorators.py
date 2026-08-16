

import time
from functools import wraps


def log_execution(func):
    """
    decorator that log when a function starts and finishes.
    """
    @wraps(func) # keep idenity of the original function
    def wrapper(*args, **kwargs):
        start = time.perf_counter()

        print(f"[Start] {func.__name__}")

        result = func(*args, **kwargs)

        end = time.perf_counter()

        print(f"[End]] {func.__name__}")

        print(f"{end - start:.4f} seconds")

        return result 

    return wrapper




