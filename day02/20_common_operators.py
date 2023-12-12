from random import shuffle, randint

for num in range(3):
    print(f'Number: {num}')

my_list = list(range(0, 13, 2))

print(my_list)  # [0, 2, 4, 6, 8, 10, 12]

my_string = 'abcdef'

for item in enumerate(my_string):
    print(f'{item}')

for index, char in enumerate(my_string):
    print(f'{char} is at index {index}')

numbers = [0, 1, 2, 3]
characters = ['a', 'b', 'c', 'd']

for item in zip(numbers, characters):
    print(f'{item}')

exceed_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for item in zip(numbers, characters, exceed_numbers):
    print(f'{item}')

my_tuple = (1, 2, 3, 4)

print(2 in numbers)  # Works for dictionary and set and tuples

print(3 in my_tuple)

print(min(numbers))

print(max(numbers))

shuffle(numbers)

print(numbers)

print(randint(0, 130))

my_input = input('Enter the number: ')

print(my_input)

print(type(my_input))

print(type(int(my_input)))
