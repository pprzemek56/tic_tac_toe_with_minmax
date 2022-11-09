from globals import BOARD, print_board


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
    else:
        computer = "O"

    print("GOOD LUCK!")
    print("EACH SQUARE IS NUMERATED FROM 0 TO 8")
    print("STARTING FROM TOP LEFT CORNER")
    print("YOU CAN NOT ACCESS TAKEN SQUARE!")
    print_board()
