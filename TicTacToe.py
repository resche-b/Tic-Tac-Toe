board = [" ", " ", " "], [" ", " ", " "], [" ", " ", " "]
turns = 0


def check_row():
    if (board[0][0] == "O" and board[0][1] == "O" and board[0][2] == "O") or (
            board[0][0] == "X" and board[0][1] == "X" and board[0][2] == "X"):
        return 1

    if (board[1][0] == "O" and board[1][1] == "O" and board[1][2] == "O") or (
            board[1][0] == "X" and board[1][1] == "X" and board[1][2] == "X"):
        return 1

    if (board[2][0] == "O" and board[2][1] == "O" and board[2][2] == "O") or (
            board[2][0] == "X" and board[2][1] == "X" and board[2][2] == "X"):
        return 1

    return 0


def check_column():
    if (board[0][0] == "O" and board[1][0] == "O" and board[2][0] == "O") or (
            board[0][0] == "X" and board[1][0] == "X" and board[2][0] == "X"):
        return 1

    if (board[0][1] == "O" and board[1][1] == "O" and board[2][1] == "O") or (
            board[0][1] == "X" and board[1][1] == "X" and board[2][1] == "X"):
        return 1

    if (board[0][2] == "O" and board[1][2] == "O" and board[2][2] == "O") or (
            board[0][2] == "X" and board[1][2] == "X" and board[2][2] == "X"):
        return 1

    return 0


def check_diagonal():
    if (board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "O") or (
            board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X"):
        return 1

    if (board[0][2] == "O" and board[1][1] == "O" and board[2][0] == "O") or (
            board[0][2] == "X" and board[1][1] == "X" and board[2][0] == "X"):
        return 1

    return 0


while True:

    while True:

        i = input("Player 1 enter row: ")
        k = input("Player 1 enter column: ")
        if board[int(i)][int(k)] != " ":
            print("Invalid location")
        else:
            break

    board[int(i)][int(k)] = "X"
    turns += 1

    for row in range(len(board)):
        print("|" + board[row][0] + "|" + board[row][1] + "|" + board[row][2] + "|")

    if turns >= 9:
        print("Tie game!")
        break

    if check_row() == 1 or check_column() == 1 or check_diagonal() == 1:
        print("Winner: Player 1!")
        break

    while True:

        i = input("Player 2 enter row: ")
        k = input("Player 2 enter column: ")
        if board[int(i)][int(k)] != " ":
            print("Invalid location")
        else:
            break

    board[int(i)][int(k)] = "O"
    turns += 1

    for row in range(len(board)):
        print("|" + board[row][0] + "|" + board[row][1] + "|" + board[row][2] + "|")

    if check_row() == 1 or check_column() == 1 or check_diagonal() == 1:
        print("Winner: Player 2!")
        break

    if turns >= 9:
        print("Tie game!")
        break
