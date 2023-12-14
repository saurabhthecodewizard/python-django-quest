game_list = [0, 1, 2]


def display_game(display_game_list):
    print("Current list:-")
    print(display_game_list)


def input_choice(message: str, accepted_values: list):
    choice = 'wrong'
    while choice not in accepted_values:
        choice = input(f"{message}: ")
        if choice not in accepted_values:
            print("Invalid choice")

    return choice


def position_choice():
    return int(input_choice("Enter a number between (0, 1, 2): ", ['0', '1', '2']))


def replacement_choice(replacement_game_list: list, position: int):
    user_replacement = input("Enter a string to replace: ")
    replacement_game_list[position] = user_replacement


def game_on_choice():
    choice = input_choice("Keep Playing? (Y or N): ", ['Y', 'N'])
    if choice == 'Y':
        return True
    return False


display_game(game_list)
print(replacement_choice(game_list, position_choice()))
display_game(game_list)

while game_on_choice():
    display_game(game_list)
    print(replacement_choice(game_list, position_choice()))
    display_game(game_list)


