from computers import computer_move, game_over


def single_game(board):
    print("SINGLE PLAYER MODE")
    print("CHOOSE THE DIFFICULTY LEVEL")
    print("1 ----- EASY")
    print("2 ----- HARD")
    level = input("LEVEL: ")
    while level != "1" and level != "2":
        print("Wrong choice, try again!")
        print("1 ----- EASY")
        print("2 ----- HARD")

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
    else:
        computer = "O"
        counter = 1

    print("GOOD LUCK!")
    print("EACH SQUARE IS NUMERATED FROM 0 TO 8")
    print("STARTING FROM TOP LEFT CORNER")
    print("YOU CAN NOT ACCESS TAKEN SQUARE!")

    while True:
        if counter % 2 == 0:
            # player turn
            if counter == 0:
                board.print_board()
            try:
                choice = int(input("PLAYER TURN: "))
                i = int(choice / 3)
                j = choice % 3
                if not board.valid_choice(i, j):
                    raise ValueError
            except ValueError:
                continue
            board.set_cell(i, j, player)
            board.print_board()
        else:
            # computer turn
            computer_move(board, level, computer)
            board.print_board()

        if game_over(board.board):
            if game_over(board.board) == player:
                print("CONGRATULATIONS PLAYER WIN!")
                break
            elif game_over(board.board) == computer:
                print("COMPUTER WIN!")
                break
            print("DRAW!!")
        counter += 1
