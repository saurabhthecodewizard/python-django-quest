# result = input("Enter number: ")
#
# print(result)
#
# position_index = int(input("Enter index: "))
#
# print(type(position_index))


def user_choice():
    accepted_values = [1, 2, 3]
    input_valid = False
    choice = 'WRONG'
    while not choice.isdigit() or not input_valid:
        choice = input("Please enter a number between 1 and 3: ")
        if not choice.isdigit():
            print("Incorrect input!")
        if choice.isdigit():
            if int(choice) in accepted_values:
                input_valid = True
            else:
                input_valid = False
                print("Out Of Range")

    return int(choice) - 1


print(user_choice())
