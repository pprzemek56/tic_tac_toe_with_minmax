from globals import BOARD, print_board


def multi_game():
    print("MULTIPLAYER MODE")
    print("FIRST PLAYER CHOOSES X OR O")
    player_1 = input("Your choice: ").upper()
    while player_1 != "O" and player_1 != "X":
        print("Wrong choice, try again!")
        player_1 = input("Your choice: ").upper()

    if player_1 == "O":
        player_2 = "X"
    else:
        player_2 = "O"

    print("GOOD LUCK!")
    print("EACH SQUARE IS NUMERATED FROM 0 TO 8")
    print("STARTING FROM TOP LEFT CORNER")
    print("YOU CAN NOT ACCESS TAKEN SQUARE!")
    print_board()
    counter = 0
    while True:
        if counter % 2 == 0:
            # player_1 turn
            try:
                choice = int(input("PLAYER 1 TURN: "))
                if not valid_choice(choice):
                    raise ValueError
            except ValueError:
                continue
            make_move(choice, player_1)
            print_board()
            if check_win():
                print("CONGRATULATIONS FOR PLAYER 1!")
                break
        else:
            # player_2 turn
            try:
                choice = int(input("PLAYER 2 TURN: "))
                if not valid_choice(choice):
                    raise ValueError
            except ValueError:
                continue
            make_move(choice, player_2)
            print_board()
            if check_win():
                print("CONGRATULATIONS FOR PLAYER 2!")
                break
        if counter == 8:
            print("DRAW!")
            break
        counter += 1



def check_win():
    return BOARD[0][0] == BOARD[0][1] == BOARD[0][2] != " " or \
           BOARD[1][0] == BOARD[1][1] == BOARD[1][2] != " " or \
           BOARD[2][0] == BOARD[2][1] == BOARD[2][2] != " " or \
           BOARD[0][0] == BOARD[1][0] == BOARD[2][0] != " " or \
           BOARD[0][1] == BOARD[1][1] == BOARD[2][1] != " " or \
           BOARD[0][2] == BOARD[1][2] == BOARD[2][2] != " " or \
           BOARD[0][0] == BOARD[1][1] == BOARD[2][2] != " " or \
           BOARD[0][2] == BOARD[1][1] == BOARD[2][0] != " "


def make_move(choice, player):
    i = int(choice / 3)
    j = choice % 3
    BOARD[i][j] = player


def valid_choice(choice):
    if choice < 0 or choice > 8:
        return False

    i = int(choice / 3)
    j = choice % 3

    if BOARD[i][j] != " ":
        return False

    return True
