my_tuple = (1, 2, 3)

print(my_tuple)  # (1, 2, 3)

my_tuple = ('a', 'a', 'a', 'b')

print(my_tuple.count('a'))  # 3

print(my_tuple.index('a'))  # 0

print(my_tuple.index('b'))  # 3

# my_tuple[0] = 'NEW'  # TypeError: 'tuple' object does not support item assignment
