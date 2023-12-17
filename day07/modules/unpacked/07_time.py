import time
import timeit


def one(n):
    return [str(num) for num in range(n)]


def two(n):
    return list(map(str, range(n)))


start = time.time()

result = one(10000000)

end = time.time()

print(end - start)

start = time.time()

res = two(10000000)

end = time.time()

print(end - start)

stmt = """
one(10000000)
"""

setup = """
def one(n):
    return [str(num) for num in range(n)]
"""

print(timeit.timeit(stmt, setup, number=5))

stmt = """
two(10000000)
"""

setup = """
def two(n):
    return list(map(str, range(n)))
"""

print(timeit.timeit(stmt, setup, number=5))
