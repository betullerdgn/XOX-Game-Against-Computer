game_chart = [' ' for x in range(10)]


def print_chart():
    print(' ' + game_chart[1] + ' ' + '|' + ' ' + game_chart[2] + ' ' + '|' + ' ' + game_chart[3])
    print("------------")
    print(' ' + game_chart[4] + ' ' + '|' + ' ' + game_chart[5] + ' ' + '|' + ' ' + game_chart[6])
    print("------------")
    print(' ' + game_chart[7] + ' ' + '|' + ' ' + game_chart[8] + ' ' + '|' + ' ' + game_chart[9])


def fill_location(letter, location):
    game_chart[location] = letter


def is_empty(location):
    return game_chart[location] == ' '


def chart_is_full():
    if game_chart.count(' ') > 1:
        return False
    else:
        return True


def winner(game_chart, letter):
    return (game_chart[1] == letter and game_chart[2] == letter and game_chart[3] == letter) or (
                game_chart[4] == letter and game_chart[5] == letter and game_chart[6] == letter) or (
                       game_chart[7] == letter and game_chart[8] == letter and game_chart[9] == letter) or (
                       game_chart[1] == letter and game_chart[4] == letter and game_chart[7] == letter) or (
                       game_chart[2] == letter and game_chart[5] == letter and game_chart[8] == letter) or (
                       game_chart[3] == letter and game_chart[6] == letter and game_chart[9] == letter) or (
                       game_chart[1] == letter and game_chart[5] == letter and game_chart[9] == letter) or (
                       game_chart[3] == letter and game_chart[5] == letter and game_chart[7] == letter)


def gamer_input():
    location = int(input("Enter a location between 1-9 :"))
    if is_empty(location):
        fill_location('X', location)
        if winner(game_chart, 'X'):
            print_chart()
            print("Congratulations You Won!")
            exit()
        print_chart()
    else:
        print("The location you entered is full, enter another location :")
        gamer_input()


def computer_input():
    import random
    empty_locations = [location for location, letter in enumerate(game_chart) if letter == ' ' and location != 0]

    move = 0

    for letter in ['O', 'X']:
        for i in empty_locations:
            duplicate_board = game_chart[:]
            duplicate_board[i] = letter
            if winner(duplicate_board, letter):
                move = i
                return move

    corners = []

    for i in empty_locations:
        if i in [1, 3, 7, 9]:
            corners.append(i)

    if len(corners) > 0:
        move = random.choice(corners)
        return move

    if 5 in empty_locations:
        move = 5
        return move

    inside = []

    for i in empty_locations:
        if i in [2, 4, 6, 8]:
            inside.append(i)

    if len(inside) > 0:
        move = random.choice(inside)
        return move


def game():
    print("Welcome to XOX Game")
    print_chart()

    while not chart_is_full():

        gamer_input()
        if chart_is_full():
            print("Game Ended in Draw, No Winner!")
            exit()

        print("-------------------------------")

        computers_move = computer_input()
        fill_location('O', computers_move)
        if winner(game_chart, 'O'):
            print_chart()
            print("Computer Won, Try Again :)")
            exit()

        print_chart()
        if chart_is_full():
            print("Game Ended in Draw, No Winner!")
            exit()

        print("-------------------------------")


game()
