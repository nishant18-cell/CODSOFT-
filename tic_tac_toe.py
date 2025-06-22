## Author: Nishant Garg
# Project: CodSoft AI Internship Task 2
# Description: Tic-Tac-Toe game with unbeatable AI using Minimax algorithm
# Language: Python

import math

# Function to print the game board
def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

# Function to check if someone has won
def check_winner(board):
    # Check rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
    return None

# Check if the board is full (for draw)
def is_full(board):
    for row in board:
        if " " in row:
            return False
    return True

# Minimax algorithm for AI
def minimax(board, is_max):
    winner = check_winner(board)
    if winner == "O":
        return 1
    elif winner == "X":
        return -1
    elif is_full(board):
        return 0

    if is_max:
        best = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    score = minimax(board, False)
                    board[i][j] = " "
                    best = max(best, score)
        return best
    else:
        best = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    score = minimax(board, True)
                    board[i][j] = " "
                    best = min(best, score)
        return best

# AI chooses the best move
def best_move(board):
    best_score = -math.inf
    move = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                score = minimax(board, False)
                board[i][j] = " "
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

# Game starts here
board = [[" " for _ in range(3)] for _ in range(3)]
print("Welcome to Tic-Tac-Toe!")
print("You are X. The computer is O.")
print_board(board)

while True:
    # Player move
    try:
        row = int(input("Enter row (0-2): "))
        col = int(input("Enter col (0-2): "))
    except:
        print("Invalid input. Enter numbers 0, 1, or 2.")
        continue

    if row not in [0, 1, 2] or col not in [0, 1, 2]:
        print("Invalid position. Try again.")
        continue

    if board[row][col] != " ":
        print("That spot is already taken. Try another.")
        continue

    board[row][col] = "X"

    winner = check_winner(board)
    if winner:
        print_board(board)
        print(f"{winner} wins!")
        break
    if is_full(board):
        print_board(board)
        print("It's a draw!")
        break

    # AI move
    ai_row, ai_col = best_move(board)
    board[ai_row][ai_col] = "O"
    print("\nComputer played:")
    print_board(board)

    winner = check_winner(board)
    if winner:
        print(f"{winner} wins!")
        break
    if is_full(board):
        print("It's a draw!")
        break