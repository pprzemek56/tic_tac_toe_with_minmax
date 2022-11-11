def multi_game(board):
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
    board.print_board()
    counter = 0
    while True:
        if counter % 2 == 0:
            # player_1 turn
            try:
                choice = int(input("PLAYER 1 TURN: "))
                i = int(choice / 3)
                j = choice % 3
                if not board.valid_choice(i, j):
                    raise ValueError
            except ValueError:
                continue
            board.set_cell(i, j, player_1)
            board.print_board()
            if board.check_win():
                print("CONGRATULATIONS FOR PLAYER 1!")
                break
        else:
            # player_2 turn
            try:
                choice = int(input("PLAYER 2 TURN: "))
                i = int(choice / 3)
                j = choice % 3
                if not board.valid_choice(i, j):
                    raise ValueError
            except ValueError:
                continue
            board.set_cell(i, j, player_2)
            board.print_board()
            if board.check_win():
                print("CONGRATULATIONS FOR PLAYER 2!")
                break
        if counter == 8:
            print("DRAW!")
            break
        counter += 1
