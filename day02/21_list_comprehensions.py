letters = 'hello'

my_list = []

for letter in letters:
    my_list.append(letter)

print(my_list)

my_comprehended_list = [letter for letter in letters]

print(my_comprehended_list)

numbers = [number for number in range(0, 13, 2)]

print(numbers)

squares = [square ** 2 for square in range(4)]

print(squares)

celcius = [0, 10, 20, 44.6, 66.2, 83.5]

fahrenheit = [((9 / 5) * num + 32) for num in celcius]

print(fahrenheit)

temp_list = []

for x in [1, 2, 3]:
    for y in [1, 10, 100]:
        temp_list.append(x * y)


print(temp_list)

comprehended_temp_list = [x * y for x in [1, 2, 3] for y in [1, 10, 100]]

print(comprehended_temp_list)

print([temp for temp in range(1, 50) if temp % 3 == 0])

my_string = 'Print every word in this sentence that has even number of letters'

print([word for word in my_string.split(' ') if len(word) % 2 == 0])

print([word[0] for word in my_string.split(' ')])
