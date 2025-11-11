import tkinter as tk
from tkinter import font
from tic_tac_toe_gui import TicTacToeGUI
from tetris import TetrisGame

class MainMenu:
    def __init__(self, master):
        self.master = master
        self.master.title("Game Collection")
        self.master.geometry("400x400")

        self.title_font = font.Font(family="Helvetica", size=24, weight="bold")
        self.button_font = font.Font(family="Helvetica", size=12)

        self.show_main_menu()

    def clear_window(self):
        for widget in self.master.winfo_children():
            widget.destroy()

    def show_main_menu(self):
        self.clear_window()
        self.master.geometry("400x400")
        self.master.title("Game Collection")
        title_label = tk.Label(self.master, text="Game Collection", font=self.title_font, pady=20)
        title_label.pack()

        tic_tac_toe_button = tk.Button(self.master, text="Tic Tac Toe", font=self.button_font, command=self.start_tic_tac_toe)
        tic_tac_toe_button.pack(pady=10)

        tetris_button = tk.Button(self.master, text="Tetris", font=self.button_font, command=self.start_tetris)
        tetris_button.pack(pady=10)

    def start_tic_tac_toe(self):
        self.clear_window()
        TicTacToeGUI(self.master)

    def start_tetris(self):
        self.clear_window()
        TetrisGame(self.master)

def main():
    root = tk.Tk()
    MainMenu(root)
    root.mainloop()

if __name__ == "__main__":
    main()
