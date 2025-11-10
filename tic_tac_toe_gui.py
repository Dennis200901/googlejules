
import tkinter as tk
from tkinter import messagebox

def check_win(board, player):
    """Checks if a player has won."""
    # Check rows
    for row in board:
        if all(s == player for s in row):
            return True
    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_full(board):
    """Checks if the board is full."""
    return all(cell != ' ' for row in board for cell in row)

class TicTacToeGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic Tac Toe")
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_widgets()

    def create_widgets(self):
        self.button_frame = tk.Frame(self.master)
        self.button_frame.pack()

        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.button_frame, text=' ', font=('normal', 20), width=5, height=2,
                                             command=lambda row=i, col=j: self.on_button_click(row, col))
                self.buttons[i][j].grid(row=i, column=j)

        self.reset_button = tk.Button(self.master, text="Reset", command=self.reset_game)
        self.reset_button.pack()

    def on_button_click(self, row, col):
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)

            if check_win(self.board, self.current_player):
                messagebox.showinfo("Tic Tac Toe", f"Player {self.current_player} wins!")
                self.disable_buttons()
            elif is_full(self.board):
                messagebox.showinfo("Tic Tac Toe", "It's a draw!")
                self.disable_buttons()
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'

    def disable_buttons(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(state=tk.DISABLED)

    def reset_game(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text=' ', state=tk.NORMAL)

def main():
    root = tk.Tk()
    TicTacToeGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
