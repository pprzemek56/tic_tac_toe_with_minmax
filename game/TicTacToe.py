import sys

from multiplayer import multi_game
from singleplayer import single_game

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
                multi_game()
            case "2":
                single_game()
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


if __name__ == "__main__":
    main()
