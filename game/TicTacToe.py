import sys

from multiplayer import multi_game
from singleplayer import single_game

from board import Board


def main():
    game()


def game():
    print("WELLCOME IN TIC TAC TOE")
    while True:
        board = Board([[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]])
        print("CHOSE 1 FOR MULTIPLAYER GAME")
        print("CHOSE 2 FOR SINGLE PLAYER GAME")
        print("CHOSE 0 FOR END GAME")
        chose_game = input()
        match chose_game:
            case "1":
                multi_game(board)
            case "2":
                single_game(board)
            case "0":
                print("Thank you, for playing!")
                sys.exit()
            case other:
                print("No match found")
                print("Try again!")



if __name__ == "__main__":
    main()
