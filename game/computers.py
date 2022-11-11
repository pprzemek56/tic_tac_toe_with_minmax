import random


def computer_move(board, level, computer):
    match level:
        case "1":
            easy(board, computer)
        case "2":
            medium()
        case "3":
            hard(board, computer)


def easy(board, computer):
    available_moves = []
    for i in range(3):
        for j in range(3):
            if board.get_cell(i, j) == " ":
                available_moves.append([i, j])

    move = random.choice(available_moves)
    board.set_cell(move[0], move[1], computer)


def medium():
    ...


def hard(board, computer):
    max_value = -10
    best_move = []
    position = board.board
    alpha = -10
    beta = 10
    for i in range(3):
        for j in range(3):
            if board.get_cell(i, j) != " ":
                continue
            temp_board = copy_board(position)
            result = minimax(temp_board, 9, alpha, beta, True, computer)
            alpha = max(alpha, result)
            if beta <= alpha:
                break
            if result > max_value:
                max_value = result
                best_move = [i, j]

    board.set_cell(best_move[0], best_move[1], computer)


def minimax(position, depth, alpha, beta, maximizing_player, computer):
    if depth == 0 or game_over(position) == "X" or game_over(position) == "O":
        if game_over(position) == "D":
            return 0
        elif game_over(position) == computer:
            return 1
        return -1
    if maximizing_player:
        max_evaluation = -10
        for i in range(3):
            for j in range(3):
                if position[i][j] != " ":
                    continue
                temp_board = copy_board(position)
                temp_board[i][j] = computer
                result = minimax(temp_board, depth - 1, alpha, beta, False, computer)
                alpha = max(alpha, result)
                if beta <= alpha:
                    break
                max_evaluation = max(max_evaluation, result)
        return max_evaluation
    else:
        min_evaluation = 10
        if computer == "X":
            player = "O"
        else:
            player = "X"
        for i in range(3):
            for j in range(3):
                if position[i][j] != " ":
                    continue
                temp_board = [position[i].copy() for i in range(3)]
                temp_board[i][j] = player
                result = minimax(temp_board, depth - 1, alpha, beta, True, computer)
                beta = min(beta, result)
                if beta <= alpha:
                    break
                min_evaluation = min(min_evaluation, result)
        return min_evaluation


def game_over(position):
    if position[0][0] == position[0][1] == position[0][2] != " " or \
            position[0][0] == position[1][1] == position[2][2] != " " or \
            position[0][0] == position[1][0] == position[2][0] != " ":
        return position[0][0]
    elif position[1][1] == position[0][1] == position[2][1] != " " or \
            position[1][1] == position[1][0] == position[1][2] != " " or \
            position[1][1] == position[2][0] == position[0][2] != " ":
        return position[1][1]
    elif position[2][2] == position[1][2] == position[0][2] != " " or \
            position[2][2] == position[2][1] == position[2][0] != " ":
        return position[2][2]
    return "D"


def copy_board(position):
    new_board = [position[i].copy() for i in range(3)]
    return new_board
