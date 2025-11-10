import tkinter as tk
from tkinter import messagebox, font
from game_logic import TicTacToeGame
from trophy_manager import TrophyManager

class TicTacToeGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic Tac Toe")
        self.master.geometry("400x400")
        self.trophy_manager = TrophyManager()
        self.game = None
        self.buttons = None
        self.game_mode = None
        self.difficulty = None
        self.board_size = None

        # Custom fonts
        self.title_font = font.Font(family="Helvetica", size=24, weight="bold")
        self.button_font = font.Font(family="Helvetica", size=12)
        self.board_font = font.Font(family="Helvetica", size=20)

        self.show_main_menu()

    def clear_window(self):
        for widget in self.master.winfo_children():
            widget.destroy()

    def show_main_menu(self):
        self.clear_window()
        self.master.title("Tic Tac Toe - Main Menu")

        title_label = tk.Label(self.master, text="Tic Tac Toe", font=self.title_font, pady=20)
        title_label.pack()

        single_player_button = tk.Button(self.master, text="Single Player", font=self.button_font, command=self.show_difficulty_selection)
        single_player_button.pack(pady=10)

        multi_player_button = tk.Button(self.master, text="Multiplayer", font=self.button_font, command=lambda: self.show_board_selection('multiplayer'))
        multi_player_button.pack(pady=10)

        trophy_hall_button = tk.Button(self.master, text="Trophy Hall", font=self.button_font, command=self.show_trophy_hall)
        trophy_hall_button.pack(pady=10)

    def show_difficulty_selection(self):
        self.clear_window()
        self.master.title("Select Difficulty")

        title_label = tk.Label(self.master, text="Select Difficulty", font=self.title_font, pady=20)
        title_label.pack()

        difficulties = [("Easy", "easy"), ("Medium", "medium"), ("Hard", "hard")]
        for text, diff in difficulties:
            btn = tk.Button(self.master, text=text, font=self.button_font, command=lambda d=diff: self.set_difficulty_and_show_board(d))
            btn.pack(pady=5)

        back_button = tk.Button(self.master, text="Back", font=self.button_font, command=self.show_main_menu)
        back_button.pack(pady=20)

    def set_difficulty_and_show_board(self, difficulty):
        self.difficulty = difficulty
        self.show_board_selection('single_player')

    def show_board_selection(self, game_mode):
        self.game_mode = game_mode
        self.clear_window()
        self.master.title("Select Board Size")

        title_label = tk.Label(self.master, text="Select Board Size", font=self.title_font, pady=20)
        title_label.pack()

        sizes = [("3x3", 3), ("5x5", 5)]
        for text, size in sizes:
            btn = tk.Button(self.master, text=text, font=self.button_font, command=lambda s=size: self.start_game(s))
            btn.pack(pady=5)

        back_command = self.show_difficulty_selection if self.game_mode == 'single_player' else self.show_main_menu
        back_button = tk.Button(self.master, text="Back", font=self.button_font, command=back_command)
        back_button.pack(pady=20)

    def show_trophy_hall(self):
        self.clear_window()
        self.master.title("Trophy Hall")

        trophies = self.trophy_manager.get_trophies()

        title_label = tk.Label(self.master, text="Trophy Hall", font=self.title_font, pady=20)
        title_label.pack()

        trophy_label = tk.Label(self.master, text=f"🏆 Trophies: {trophies} 🏆", font=("Helvetica", 18), pady=20)
        trophy_label.pack()

        back_button = tk.Button(self.master, text="Back to Main Menu", font=self.button_font, command=self.show_main_menu)
        back_button.pack(pady=20)

    def start_game(self, board_size):
        self.board_size = board_size
        self.game = TicTacToeGame(size=board_size)
        self.clear_window()
        self.master.title(f"Tic Tac Toe - {board_size}x{board_size}")
        self.create_board_widgets()

    def create_board_widgets(self):
        self.button_frame = tk.Frame(self.master)
        self.button_frame.pack(pady=10)

        self.buttons = [[None for _ in range(self.board_size)] for _ in range(self.board_size)]

        for i in range(self.board_size):
            for j in range(self.board_size):
                self.buttons[i][j] = tk.Button(self.button_frame, text=' ', font=self.board_font, width=4, height=2,
                                             command=lambda row=i, col=j: self.on_button_click(row, col))
                self.buttons[i][j].grid(row=i, column=j)

        self.status_label = tk.Label(self.master, text=f"Player {self.game.current_player}'s turn", font=self.button_font)
        self.status_label.pack(pady=10)

        control_frame = tk.Frame(self.master)
        control_frame.pack(pady=10)

        reset_button = tk.Button(control_frame, text="Reset Game", font=self.button_font, command=lambda: self.start_game(self.board_size))
        reset_button.pack(side=tk.LEFT, padx=10)

        back_button = tk.Button(control_frame, text="Main Menu", font=self.button_font, command=self.show_main_menu)
        back_button.pack(side=tk.LEFT, padx=10)

    def on_button_click(self, row, col):
        if self.game.board[row][col] != ' ':
            return

        player = self.game.current_player
        if self.game.make_move(row, col):
            self.update_board()
            if self.check_game_over(player):
                return

            self.game.switch_player()
            self.status_label.config(text=f"Player {self.game.current_player}'s turn")

            if self.game_mode == 'single_player' and self.game.current_player == 'O':
                self.master.after(500, self.computer_move)

    def computer_move(self):
        if self.game.is_full(): return

        move = self.game.get_computer_move(self.difficulty)
        if move:
            row, col = move
            player = self.game.current_player
            if self.game.make_move(row, col):
                self.update_board()
                if self.check_game_over(player):
                    return
                self.game.switch_player()
                self.status_label.config(text=f"Player {self.game.current_player}'s turn")

    def check_game_over(self, player):
        if self.game.check_win(player):
            self.handle_win(player)
            return True
        elif self.game.is_full():
            self.handle_draw()
            return True
        return False

    def handle_win(self, player):
        self.disable_buttons()
        self.status_label.config(text=f"Player {player} wins!")
        if self.game_mode == 'single_player' and player == 'X':
            self.trophy_manager.add_trophies(10)
            messagebox.showinfo("Winner!", f"Congratulations Player {player}! You win 10 trophies!")
        else:
            messagebox.showinfo("Winner!", f"Player {player} wins!")

    def handle_draw(self):
        self.disable_buttons()
        self.status_label.config(text="It's a draw!")
        messagebox.showinfo("Draw", "The game is a draw!")

    def update_board(self):
        for i in range(self.board_size):
            for j in range(self.board_size):
                self.buttons[i][j].config(text=self.game.board[i][j])

    def disable_buttons(self):
        for i in range(self.board_size):
            for j in range(self.board_size):
                self.buttons[i][j].config(state=tk.DISABLED)

def main():
    root = tk.Tk()
    TicTacToeGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
