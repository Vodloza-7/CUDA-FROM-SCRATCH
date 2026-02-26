from numba import jit   # the module that enabled numba execution of functions on the CPU
import math as m 

@jit
def hypot(x, y):
    # implementation of hypot can be found here https://en.wikipedia.org/wiki/Hypot
    x = abs(x)
    y = abs(y)
    t = min(x, y)
    x = max(x, y)
    t = t / x
    return x * m.sqrt(1 + t * t)

print(hypot(3.0, 4.0))