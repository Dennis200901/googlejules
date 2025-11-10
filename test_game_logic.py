import unittest
from game_logic import TicTacToeGame

class TestTicTacToeGame(unittest.TestCase):
    def test_3x3_win_horizontal(self):
        game = TicTacToeGame(size=3)
        game.board = [['X', 'X', 'X'], [' ', 'O', ' '], [' ', ' ', 'O']]
        self.assertTrue(game.check_win('X'))

    def test_3x3_win_vertical(self):
        game = TicTacToeGame(size=3)
        game.board = [['X', 'O', ' '], ['X', 'O', ' '], ['X', ' ', 'O']]
        self.assertTrue(game.check_win('X'))

    def test_3x3_win_diagonal(self):
        game = TicTacToeGame(size=3)
        game.board = [['X', 'O', ' '], [' ', 'X', ' '], [' ', 'O', 'X']]
        self.assertTrue(game.check_win('X'))

    def test_5x5_win_horizontal(self):
        game = TicTacToeGame(size=5)
        game.board[0] = ['X', 'X', 'X', 'X', 'X']
        self.assertTrue(game.check_win('X'))

    def test_5x5_win_vertical(self):
        game = TicTacToeGame(size=5)
        for i in range(5):
            game.board[i][0] = 'X'
        self.assertTrue(game.check_win('X'))

    def test_5x5_win_diagonal(self):
        game = TicTacToeGame(size=5)
        for i in range(5):
            game.board[i][i] = 'X'
        self.assertTrue(game.check_win('X'))

    def test_is_full(self):
        game = TicTacToeGame(size=3)
        game.board = [['X', 'O', 'X'], ['X', 'O', 'O'], ['O', 'X', 'X']]
        self.assertTrue(game.is_full())

    def test_get_empty_cells(self):
        game = TicTacToeGame(size=3)
        game.board = [['X', 'O', 'X'], ['X', ' ', 'O'], ['O', 'X', 'X']]
        self.assertEqual(game.get_empty_cells(), [(1, 1)])

    def test_easy_move(self):
        game = TicTacToeGame(size=3)
        game.board = [['X', 'O', 'X'], ['O', 'X', 'O'], [' ', ' ', ' ']]
        move = game.get_computer_move('easy')
        self.assertIn(move, [(2, 0), (2, 1), (2, 2)])

    def test_medium_move_win(self):
        game = TicTacToeGame(size=3)
        game.current_player = 'O'
        game.board = [['O', 'O', ' '], ['X', 'X', ' '], [' ', ' ', ' ']]
        move = game.get_computer_move('medium')
        self.assertEqual(move, (0, 2))

    def test_medium_move_block(self):
        game = TicTacToeGame(size=3)
        game.current_player = 'O'
        game.board = [['X', 'X', ' '], ['O', ' ', ' '], [' ', ' ', ' ']]
        move = game.get_computer_move('medium')
        self.assertEqual(move, (0, 2))

    def test_hard_move_win(self):
        game = TicTacToeGame(size=3)
        game.current_player = 'O'
        game.board = [['O', 'O', ' '], ['X', 'X', ' '], [' ', ' ', ' ']]
        move = game.get_computer_move('hard')
        self.assertEqual(move, (0, 2))

    def test_hard_move_block(self):
        game = TicTacToeGame(size=3)
        game.current_player = 'O'
        game.board = [['X', 'X', ' '], ['O', ' ', ' '], [' ', ' ', ' ']]
        move = game.get_computer_move('hard')
        self.assertEqual(move, (0, 2))

if __name__ == '__main__':
    unittest.main()
