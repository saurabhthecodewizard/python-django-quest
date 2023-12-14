import random


print('Welcome to Tic Tac Toe!')


def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'


def display_board(game_board: list):
    print('\n' * 2)
    print('Positions:-')
    print('7 | 8 | 9')
    print('---------')
    print('4 | 5 | 6')
    print('---------')
    print('1 | 2 | 3')
    print()
    print(game_board[7] + ' | ' + game_board[8] + ' | ' + game_board[9])
    print('---------')
    print(game_board[4] + ' | ' + game_board[5] + ' | ' + game_board[6])
    print('---------')
    print(game_board[1] + ' | ' + game_board[2] + ' | ' + game_board[3])


def player_ready_to_play():
    ready_to_play = ' '
    while ready_to_play not in ['Y', 'N']:
        ready_to_play = input('Are you ready to play? Enter Y or N: ')

    return ready_to_play


def player_marker_input():
    marker = ''
    while marker != 'X' and marker != 'O':
        marker = input('Player 1, choose X or O: ')

    if marker == 'X':
        return 'X', 'O'
    return 'O', 'X'


def player_index_input(game_board):
    choice = 0
    while choice not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or game_board[choice] != ' ':
        choice = int(input('Choose your position (1-9): '))

    return choice


def assign_player_marker(game_board: list, index: int, marker: str):
    game_board[index] = marker


def full_board_check(game_board):
    for i in range(1,10):
        if game_board[i] == ' ':
            return False
    return True


def win_check(game_board, mark):
    return ((game_board[7] == mark and game_board[8] == mark and game_board[9] == mark) or  # across the top
            (game_board[4] == mark and game_board[5] == mark and game_board[6] == mark) or  # across the middle
            (game_board[1] == mark and game_board[2] == mark and game_board[3] == mark) or  # across the bottom
            (game_board[7] == mark and game_board[4] == mark and game_board[1] == mark) or  # down the middle
            (game_board[8] == mark and game_board[5] == mark and game_board[2] == mark) or  # down the middle
            (game_board[9] == mark and game_board[6] == mark and game_board[3] == mark) or  # down the right side
            (game_board[7] == mark and game_board[5] == mark and game_board[3] == mark) or  # diagonal
            (game_board[9] == mark and game_board[5] == mark and game_board[1] == mark))  # diagonal


def replay():
    return input("Wanna play again? Y or N: ").lower().startswith('y')


while True:
    board = [' '] * 10
    player1, player2 = player_marker_input()
    turn = choose_first()

    print(f'Player 1 will be {player1}')
    display_board(board)
    print(f'{turn} will go first.')

    ready = player_ready_to_play()

    game_on = False
    if ready.lower().startswith('y'):
        game_on = True

    while game_on:
        display_board(board)
        print(f'Current turn: {turn}')
        if turn == 'Player 1':
            player_index = player_index_input(board)
            assign_player_marker(board, player_index, player1)

            if win_check(board, player1):
                display_board(board)
                print('Congratulations! Player 1 has won')
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print('The game is a draw')
                    break
                else:
                    turn = 'Player 2'

        else:
            player_index = player_index_input(board)
            assign_player_marker(board, player_index, player2)

            if win_check(board, player2):
                display_board(board)
                print('Congratulations! Player 2 has won')
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print('The game is a draw')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break
