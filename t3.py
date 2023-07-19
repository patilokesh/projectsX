def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_win(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(row[col] == player for row in board):
            return True

    if all(board[i][i] == player for i in range(3)):
        return True

    if all(board[i][2-i] == player for i in range(3)):
        return True

    return False

def check_draw(board):
    return all(cell != " " for row in board for cell in row)

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    player_index = 0

    while True:
        print_board(board)
        player = players[player_index]
        print(f"Player {player}, it's your turn.")

        while True:
            row = int(input("Enter row (0-2): "))
            col = int(input("Enter column (0-2): "))

            if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == " ":
                break
            else:
                print("Invalid move. Try again.")

        board[row][col] = player

        if check_win(board, player):
            print_board(board)
            print(f"Congratulations! Player {player} wins!")
            break

        if check_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        player_index = (player_index + 1) % 2

if __name__ == "__main__":
    tic_tac_toe()
