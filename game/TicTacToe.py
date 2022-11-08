BOARD = [[" ", " ", " "],
         [" ", " ", " "],
         [" ", " ", " "]]


def main():
    game()


def game():
    print_board()


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
