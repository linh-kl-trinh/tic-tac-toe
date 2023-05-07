# Tic Tac Toe

## Description
This is a simple two-player Tic Tac Toe game written in Python. The game board is a 3x3 grid and players take turns marking a space with their respective symbol ("X" or "O"). The game ends when a player gets three of their symbols in a row (horizontally, vertically, or diagonally), or if all spaces on the board are filled without either player winning.

## Functions

- `print_board(board)`: This function takes in the current state of the game board as a list of lists and prints it out in a visually pleasing format. It does this by iterating over each row and column of the board and printing out the corresponding symbol or empty space.
- `check_win(board, player)`: This function takes in the current state of the game board and the symbol of the current player and checks if that player has won the game. It does this by checking all possible winning configurations (horizontally, vertically, and diagonally) and returning `True` if any of them match the current player's symbol.
- `tic_tac_toe()`: This function initializes the game board, sets up the players and their symbols, and starts the game loop. It alternates between each player's turn and prompts them to input a row and column to mark their symbol on the board. It then checks if the game has been won or if it is a tie, and prints out the corresponding message before ending the game.

## How to play
To play the game, simply run the `tic_tac_toe()` function in a Python environment or from the command line.
