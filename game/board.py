class Board:
    def __init__(self, board):
        self.board = board

    @property
    def board(self):
        return self._board

    @board.setter
    def board(self, value):
        self._board = value

    def get_cell(self, i, j):
        return self._board[i][j]

    def set_cell(self, i, j, value):
        self._board[i][j] = value

    def print_board(self):
        for i in range(3):
            for j in range(3):
                if j != 2:
                    print(f" {self.get_cell(i, j)} |", end="")
                    continue
                print(f" {self.get_cell(i, j)}  ")
            if i != 2:
                print("-------------")
                continue
            print()

    def check_win(self):
        return self.get_cell(0, 0) == self.get_cell(0, 1) == self.get_cell(0, 2) != " " or \
               self.get_cell(1, 0) == self.get_cell(1, 1) == self.get_cell(1, 2) != " " or \
               self.get_cell(2, 0) == self.get_cell(2, 1) == self.get_cell(2, 2) != " " or \
               self.get_cell(0, 0) == self.get_cell(1, 0) == self.get_cell(2, 0) != " " or \
               self.get_cell(0, 1) == self.get_cell(1, 1) == self.get_cell(2, 1) != " " or \
               self.get_cell(0, 2) == self.get_cell(1, 2) == self.get_cell(2, 2) != " " or \
               self.get_cell(0, 0) == self.get_cell(1, 1) == self.get_cell(2, 2) != " " or \
               self.get_cell(0, 2) == self.get_cell(1, 1) == self.get_cell(2, 0) != " "

    def valid_choice(self, i, j):
        if i < 0 or i > 2 or j < 0 or j > 2 or self.get_cell(i, j) != " ":
            return False

        return True
