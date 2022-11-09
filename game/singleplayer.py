from globals import BOARD, print_board
from multiplayer import make_move, valid_choice, check_win


def single_game():
    print("SINGLE PLAYER MODE")
    print("CHOOSE THE DIFFICULTY LEVEL")
    print("1 ----- EASY")
    print("2 ----- MEDIUM")
    print("3 ----- HARD")
    level = input("LEVEL: ")
    while level != "1" and level != "2" and level != "3":
        print("Wrong choice, try again!")
        print("1 ----- EASY")
        print("2 ----- MEDIUM")
        print("3 ----- HARD")

    print("CHOOSE SIGN")
    print("X ----- COMPUTER START")
    print("O ----- PLAYER START")
    player = input("Your choice: ").upper()
    while player != "O" and player != "X":
        print("Wrong choice, try again!")
        print("CHOOSE SIGN")
        print("X ----- COMPUTER START")
        print("O ----- PLAYER START")
        player = input("Your choice: ").upper()

    if player == "O":
        computer = "X"
        counter = 0
        end = 8
    else:
        computer = "O"
        counter = 1
        end = 9

    print("GOOD LUCK!")
    print("EACH SQUARE IS NUMERATED FROM 0 TO 8")
    print("STARTING FROM TOP LEFT CORNER")
    print("YOU CAN NOT ACCESS TAKEN SQUARE!")
    print_board()

    while True:
        if counter % 2 == 0:
            # player turn
            try:
                choice = int(input("PLAYER TURN: "))
                if not valid_choice(choice):
                    raise ValueError
            except ValueError:
                continue
            make_move(choice, player)
            print_board()
            if check_win():
                print("CONGRATULATIONS FOR PLAYER!!")
                break
        else:
            # computer turn
            ...
        if counter == end:
            print("DRAW!")
            break
        counter += 1
