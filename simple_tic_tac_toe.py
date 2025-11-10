board = [[' ' for _ in range(3)] for _ in range(3)]
current_player = 'X'

def print_board():
    """Prints the Tic Tac Toe board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def get_player_input():
    """Gets and validates player input."""
    while True:
        try:
            row = int(input(f"Player {current_player}, enter row (0-2): "))
            col = int(input(f"Player {current_player}, enter col (0-2): "))
            if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == ' ':
                return row, col
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def make_move(row, col):
    """Makes a move on the board."""
    board[row][col] = current_player

def check_win():
    """Checks for a win."""
    # Check horizontal
    for r in range(3):
        if board[r][0] == board[r][1] == board[r][2] != ' ':
            return True
    # Check vertical
    for c in range(3):
        if board[0][c] == board[1][c] == board[2][c] != ' ':
            return True
    # Check diagonal
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return True
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return True
    return False

def is_full():
    """Checks if the board is full."""
    return all(cell != ' ' for row in board for cell in row)

def switch_player():
    """Switches the current player."""
    global current_player
    current_player = 'O' if current_player == 'X' else 'X'

def main():
    """Main game loop."""
    print("Welcome to Simple Tic Tac Toe!")
    while True:
        print_board()
        row, col = get_player_input()
        make_move(row, col)
        if check_win():
            print_board()
            print(f"Player {current_player} wins!")
            break
        if is_full():
            print_board()
            print("It's a draw!")
            break
        switch_player()

if __name__ == "__main__":
    main()
