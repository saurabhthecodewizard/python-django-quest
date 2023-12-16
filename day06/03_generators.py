def cube(n):
    res = []
    for x in range(n):
        res.append(x**3)
    return res


def cube_generator(n):
    """
    Generator
    Memory efficient
    """
    for x in range(n):
        yield x ** 3


for x in cube(20):
    print(x)

print(cube_generator(20)) # <generator object cube_generator at 0x000001831A5E36B0>

for x in cube_generator(20):
    print(x)

obj = cube_generator(20)

print(obj) # <generator object cube_generator at 0x000002430A8236B0>

print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
# This is an iteration
# Error when iteration is complete
