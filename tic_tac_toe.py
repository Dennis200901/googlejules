from game_logic import TicTacToeGame
from trophy_manager import TrophyManager

def print_board(board):
    """Prints the Tic Tac Toe board."""
    size = len(board)
    for row in board:
        print(" | ".join(row))
        print("-" * (size * 4 - 1))

def get_player_input(prompt):
    """Gets and validates player input."""
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_menu_choice(prompt, options):
    """Gets and validates a menu choice."""
    while True:
        choice = input(prompt).lower()
        if choice in options:
            return choice
        print(f"Invalid choice. Please select from: {', '.join(options)}")

def main():
    """Main game loop."""
    trophy_manager = TrophyManager()

    print("Welcome to Tic Tac Toe!")

    game_mode = get_menu_choice("Select game mode (single/multi): ", ['single', 'multi'])

    board_size_str = get_menu_choice("Select board size (3/5): ", ['3', '5'])
    board_size = int(board_size_str)

    difficulty = 'easy'
    if game_mode == 'single':
        difficulty = get_menu_choice("Select difficulty (easy/medium/hard): ", ['easy', 'medium', 'hard'])

    game = TicTacToeGame(size=board_size)

    while True:
        print_board(game.board)

        is_computer_turn = (game_mode == 'single' and game.current_player == 'O')

        if is_computer_turn:
            print(f"Player O (Computer) is thinking...")
            move = game.get_computer_move(difficulty)
            if move:
                row, col = move
            else: # Should not happen if there are empty cells
                print("Computer has no moves left.")
                break
        else:
            prompt = f"Player {game.current_player}, enter row (0-{board_size-1}): "
            row = get_player_input(prompt)
            prompt = f"Player {game.current_player}, enter col (0-{board_size-1}): "
            col = get_player_input(prompt)

        if game.make_move(row, col):
            if game.check_win(game.current_player):
                print_board(game.board)
                winner = game.current_player
                print(f"Player {winner} wins!")
                if game_mode == 'single' and winner == 'X':
                    trophy_manager.add_trophies(10)
                    print("You earned 10 trophies!")
                break

            if game.is_full():
                print_board(game.board)
                print("It's a draw!")
                break

            game.switch_player()
        else:
            if not is_computer_turn:
                print("Invalid move. Try again.")

if __name__ == "__main__":
    main()
