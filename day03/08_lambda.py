def square(num):
    return num ** 2


my_nums = [1, 2, 3, 4, 5]

print([item for item in map(square, my_nums)])


def splicer(my_string: str):
    return 'EVEN' if len(my_string) % 2 == 0 else my_string[0]


names = ['Andy', 'Eve', 'Sally']

print(list(map(splicer, names)))

print(list(filter(lambda x: x % 2 == 0, my_nums)))
