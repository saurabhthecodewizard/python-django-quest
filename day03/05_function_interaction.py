from random import shuffle

cups = ['', '', 'O', '']

shuffle(cups)

print(cups)


def shuffle_list(my_list: list):
    shuffle(my_list)
    return my_list


def player_guess():
    guess = ''

    while guess not in ['1', '2', '3', '4']:
        guess = input('Guess a number between 1 and 4')

    return int(guess)


def check_guess(my_list: list, guess: int):
    return my_list[guess - 1] == 'O'


print(shuffle_list(cups))

input_value = player_guess()

if check_guess(cups, input_value):
    print('Correct...')
else:
    print('Wrong...')
