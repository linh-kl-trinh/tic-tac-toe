import random

def get_empty_cells(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]

def get_opponent_move(board):
    empty_cells = get_empty_cells(board)
    
    for cell in empty_cells:
        row, col = cell
        board[row][col] = "O"
        if check_win(board, "O"):
            return row, col
        board[row][col] = " "

    for cell in empty_cells:
        row, col = cell
        board[row][col] = "X"
        if check_win(board, "X"):
            return row, col
        board[row][col] = " "

    return random.choice(empty_cells)

def print_board(board):
    print("-------------")
    for i in range(3):
        print("|", end=" ")
        for j in range(3):
            print(board[i][j], "|", end=" ")
        print()
        print("-------------")

def check_win(board, player):
    for i in range(3):
        if board[i][0] == player and board[i][1] == player and board[i][2] == player:
            return True
        if board[0][i] == player and board[1][i] == player and board[2][i] == player:
            return True
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    current_player = random.choice(players)
    
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)
    
    while True:
        print(f"It's {current_player}'s turn.")
        
        if current_player == "X":
            while True:
                try:
                    row = int(input("Enter row (1, 2, or 3): ")) - 1
                    col = int(input("Enter column (1, 2, or 3): ")) - 1
                    if (0 <= row < 3) and (0 <= col < 3) and board[row][col] == " ":
                        break
                    else:
                        print("Invalid move, try again.")
                except ValueError:
                    print("Invalid input, please enter a number.")
        else:
            row, col = get_opponent_move(board)
            print(f"Opponent chooses row {row + 1} and column {col + 1}")
            
        board[row][col] = current_player
        print_board(board)
        
        if check_win(board, current_player):
            print(f"{current_player} wins!")
            break
        elif " " not in [cell for row in board for cell in row]:
            print("It's a tie!")
            break
        
        current_player = players[(players.index(current_player) + 1) % 2]

tic_tac_toe()