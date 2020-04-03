# 0 1 2 3 4 5 6 7
# 0 1 1 2 3 5 8 13

def fib(x):
    print("fib(%s)" % x)
    if x == 1 or x == 0:
        return x

    return fib(x - 1) + fib(x - 2)

print(fib(700))

"""
fib(5)
fib(4)                           + fib(3)
fib(3)             + fib(2)      + f(2)        + f(1)
f(2)        + f(1) + f(1) + f(0) + f(1) + f(0) + f(1)
f(1) + f(0) + f(1) + f(1) + f(0) + f(1) + f(0) + f(1)
"""