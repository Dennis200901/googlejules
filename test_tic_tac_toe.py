import unittest
from tic_tac_toe import check_win, is_full

class TestTicTacToe(unittest.TestCase):
    def test_check_win_horizontal(self):
        board = [['X', 'X', 'X'], [' ', 'O', ' '], [' ', ' ', 'O']]
        self.assertTrue(check_win(board, 'X'))

    def test_check_win_vertical(self):
        board = [['X', 'O', ' '], ['X', 'O', ' '], ['X', ' ', 'O']]
        self.assertTrue(check_win(board, 'X'))

    def test_check_win_diagonal(self):
        board = [['X', 'O', ' '], [' ', 'X', ' '], [' ', 'O', 'X']]
        self.assertTrue(check_win(board, 'X'))

    def test_check_win_no_winner(self):
        board = [['X', 'O', 'X'], ['X', 'O', 'O'], ['O', 'X', 'X']]
        self.assertFalse(check_win(board, 'X'))
        self.assertFalse(check_win(board, 'O'))

    def test_is_full_true(self):
        board = [['X', 'O', 'X'], ['X', 'O', 'O'], ['O', 'X', 'X']]
        self.assertTrue(is_full(board))

    def test_is_full_false(self):
        board = [['X', 'O', 'X'], ['X', ' ', 'O'], ['O', 'X', 'X']]
        self.assertFalse(is_full(board))

if __name__ == '__main__':
    unittest.main()
