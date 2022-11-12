import random


def computer_move(board, level, computer):
    match level:
        case "1":
            easy(board, computer)
        case "2":
            hard(board, computer)


def easy(board, computer):
    available_moves = []
    for i in range(3):
        for j in range(3):
            if board.get_cell(i, j) == " ":
                available_moves.append([i, j])

    move = random.choice(available_moves)
    board.set_cell(move[0], move[1], computer)


def hard(board, computer):
    max_value = -10
    best_move = tuple()
    position = board.board
    if computer == "X":
        player = "O"
    else:
        player = "X"
    for i in range(3):
        for j in range(3):
            if board.get_cell(i, j) != " ":
                continue
            temp_board = copy_board(position)
            temp_board[i][j] = computer
            result = minimax(temp_board, 2, -10, 10, False, computer, player)
            temp_board[i][j] = " "
            if result > max_value:
                max_value = result
                best_move = (i, j)

            if result == 1:
                break

    board.set_cell(best_move[0], best_move[1], computer)


def minimax(position, depth, alpha, beta, maximizing_player, computer, player):
    if game_over(position) or depth == 0:
        if game_over(position) == computer:
            return 1
        elif game_over(position) == player:
            return -1

        return 0

    if maximizing_player:
        max_evaluation = -10
        for i in range(3):
            for j in range(3):
                if position[i][j] != " ":
                    continue
                temp_board = copy_board(position)
                temp_board[i][j] = computer
                result = minimax(temp_board, depth - 1, alpha, beta, False, computer, player)
                max_evaluation = max(max_evaluation, result)
                if max_evaluation == 1:
                    return max_evaluation
                alpha = max(alpha, result)
                if beta <= alpha:
                    break
        return max_evaluation
    else:
        min_evaluation = 10
        for i in range(3):
            for j in range(3):
                if position[i][j] != " ":
                    continue
                temp_board = [position[i].copy() for i in range(3)]
                temp_board[i][j] = player
                result = minimax(temp_board, depth - 1, alpha, beta, True, computer, player)
                min_evaluation = min(min_evaluation, result)
                if min_evaluation == -1:
                    return min_evaluation
                beta = min(beta, result)
                if beta <= alpha:
                    break
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

    for i in range(3):
        for j in range(3):
            if position[i][j] == " ":
                return False
        if i == 2:
            return "D"


def copy_board(position):
    new_board = [position[i].copy() for i in range(3)]
    return new_board
