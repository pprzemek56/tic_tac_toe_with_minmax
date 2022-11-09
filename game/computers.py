import random

from globals import BOARD


def computer_move(level, computer):
    match level:
        case "1":
            easy(computer)
        case "2":
            medium()
        case "3":
            hard()


def easy(computer):
    available_moves = []
    for i in range(3):
        for j in range(3):
            if BOARD[i][j] == " ":
                available_moves.append([i, j])

    move = random.choice(available_moves)
    BOARD[move[0]][move[1]] = computer


def medium():
    ...


def hard():
    ...
