my_set = set()

print(my_set)  # set()

my_set.add(1)

my_set.add(2)

print(my_set)  # {1, 2}

my_set.add(1)

print(my_set)  # {1, 2}

my_list = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 4]

my_set = set(my_list)

print(my_list)  # [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 4]

print(my_set)  # {1, 2, 3, 4}
