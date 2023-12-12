numbers = ['one', 'two', 'three', 'four']

for number in numbers:
    print(f'Current number: {number}')

numbers = [1, 2, 3, 4, 5]

for number in numbers:
    if number % 2 == 0:
        print(f'{number} is even')
    else:
        print(f'{number} is odd')


for char in 'abcdefghi':
    print(f'Current character: {char}')

for _ in 'abcdefghi':
    print('suppressed variable')

my_lis_of_tuples = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]

for (a, b) in my_lis_of_tuples:
    print(f'Current tuple items: {a} and {b}')

my_dictionary = {
    1: 'one',
    2: 'two',
    3: 'three'
}

for key in my_dictionary:
    print(f'Current item: {key}')

for item in my_dictionary.items():
    print(f'Current item: {item}')
