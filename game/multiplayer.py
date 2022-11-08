from TicTacToe import BOARD, print_board


def game():
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
    for i in range(9):
        if i % 2 == 0:
            # player_1 turn
            try:
                choice = int(input("PLAYER 1 TURN: "))
                if valid_choice(choice):
                    make_move(choice, player_1)
                else:
                    raise ValueError
            except ValueError:
                i -= 1
                continue
        else:
            # player_2 turn
            try:
                choice = int(input("PLAYER 2 TURN: "))
                if valid_choice(choice):
                    make_move(choice, player_2)
                else:
                    raise ValueError
            except ValueError:
                i -= 1
                continue


def make_move(choice, player):
    i = int(choice / 3)
    j = choice % 3
    BOARD[i][j] = player


def valid_choice(choice):
    return False
