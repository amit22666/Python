import time
from functools import wraps


def calculate_time(func):
    @wraps(func)
    def wrapper_func(*args,**kwargs):
        print(f"executing... {func.__name__}")
        t1 = time.time()
        returned_value = func(*args,**kwargs)
        t2 = time.time()
        print(f"took {t2-t1}sec to run")
        return returned_value
        
    return wrapper_func

@calculate_time
def sq(x):
    return [i**2 for i in range(1,x)]

print(sq(8))

OUTPUT
# executing... sq
# took 8.344650268554688e-06sec to run
# [1, 4, 9, 16, 25, 36, 49]

