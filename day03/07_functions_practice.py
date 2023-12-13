def lesser_of_two_evens_or_odd(a, b):
    return min(a, b) if a % 2 == b % 2 == 0 else max(a, b)


print(lesser_of_two_evens_or_odd(2, 4))
print(lesser_of_two_evens_or_odd(2, 5))
print(lesser_of_two_evens_or_odd(7, 4))


def is_star_with_same_letter(string):
    return string[0] == string[string.find(' ') + 1]


print(is_star_with_same_letter("Lower Level"))
print(is_star_with_same_letter("Upper Level"))
print(is_star_with_same_letter("You're You"))


def capitalize_first_and_fourth_letter(string):
    return string[:2].capitalize() + string[2:].capitalize()


print(capitalize_first_and_fourth_letter('mcdonald'))

mylist = [1, 2, 3, 3, 5, 5, 6, 7, 3, 3]
another_list = [1, 2, 3, 5, 5, 6, 7, 3]

print(''.join([str(i) for i in mylist]))


def reverse_all_words_of_sentence(string: str):
    return ' '.join(string.split(' ')[::-1])
    # return ' '.join([word for word in string.split(' ')[::-1]])


print(reverse_all_words_of_sentence('Enter the new dragon'))


def is_three_next_to_three(my_list: list):
    return any([my_list[i] == my_list[i + 1] == 3 for i in range(len(my_list) - 1)])


print(is_three_next_to_three(mylist))
print(is_three_next_to_three(another_list))

hello = 'HellO'


def all_characters_thrice(string: str):
    return ''.join([char * 3 for char in string])


print(all_characters_thrice(hello))


def blackjack(a: int, b: int, c: int):
    return a + b + c if a + b + c <= 21 else (a + b + c - 10 if 11 in (a, b, c) and a + b + c > 21 else 'BUST')


print(blackjack(5, 6, 7))
print(blackjack(9, 9, 9))
print(blackjack(9, 9, 11))


def spy_game(my_list: list[int]):
    return any(my_list[i:i+3] == [0, 0, 7] for i in range(len(my_list) - 2))
    # return any([my_list[i] == 0 and my_list[i + 1] == 0 and my_list[i + 2] == 7 for i in range(len(my_list) - 2)])


print(spy_game([1, 2, 4, 0, 0, 7, 5]))
print(spy_game([1, 0, 2, 4, 0, 5, 7]))
print(spy_game([1, 7, 2, 0, 4, 5, 0]))


def count_primes(n):
    return sum(all(n % i != 0 for i in range(2, int(n**0.5) + 1)) and n > 1 for n in range(1, n + 1))


print(count_primes(100))

def print_big(letter):
    patterns = {
        'a': ['  *  ', ' * * ', '*****', '*   *', '*   *'],
        'b': ['**** ', '*   *', '**** ', '*   *', '**** '],
        'c': [' ****', '*    ', '*    ', '*    ', ' ****'],
        'd': ['**** ', '*   *', '*   *', '*   *', '**** '],
        'e': ['*****', '*    ', '*****', '*    ', '*****']
    }

    letter = letter.lower()
    if letter in patterns:
        for line in patterns[letter]:
            print(line)
    else:
        print("Letter not supported in this exercise.")


# Example usage:
print_big('a')
print()
print_big('b')
print()
print_big('c')
print()
print_big('d')
print()
print_big('e')
print()
print_big('z')  # Unsupported letter
