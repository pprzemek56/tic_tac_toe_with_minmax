import sys

import multiplayer
import singleplayer

from globals import BOARD


def main():
    game()


def game():
    print("WELLCOME IN TIC TAC TOE")
    while True:
        init_board()
        print("CHOSE 1 FOR MULTIPLAYER GAME")
        print("CHOSE 2 FOR SINGLE PLAYER GAME")
        print("CHOSE 0 FOR END GAME")
        chose_game = input()
        match chose_game:
            case "1":
                multiplayer.game()
            case "2":
                singleplayer.game()
            case "0":
                print("Thank you, for playing!")
                sys.exit()
            case other:
                print("No match found")
                print("Try again!")


def init_board():
    for i in range(3):
        for j in range(3):
            BOARD[i][j] = " "


def print_board():
    for i in range(3):
        for j in range(3):
            if j != 2:
                print(f" {BOARD[i][j]} |", end="")
                continue
            print(f" {BOARD[i][j]}  ")
        if i != 2:
            print("-------------")
            continue
        print()


if __name__ == "__main__":
    main()
