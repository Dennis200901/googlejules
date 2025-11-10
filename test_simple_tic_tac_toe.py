import unittest
import simple_tic_tac_toe

class TestSimpleTicTacToe(unittest.TestCase):
    def setUp(self):
        simple_tic_tac_toe.board = [[' ' for _ in range(3)] for _ in range(3)]
        simple_tic_tac_toe.current_player = 'X'

    def test_switch_player(self):
        self.assertEqual(simple_tic_tac_toe.current_player, 'X')
        simple_tic_tac_toe.switch_player()
        self.assertEqual(simple_tic_tac_toe.current_player, 'O')
        simple_tic_tac_toe.switch_player()
        self.assertEqual(simple_tic_tac_toe.current_player, 'X')

    def test_is_full(self):
        self.assertFalse(simple_tic_tac_toe.is_full())
        simple_tic_tac_toe.board = [['X', 'O', 'X'], ['O', 'X', 'O'], ['O', 'X', 'O']]
        self.assertTrue(simple_tic_tac_toe.is_full())

    def test_check_win_horizontal(self):
        simple_tic_tac_toe.board[0] = ['X', 'X', 'X']
        self.assertTrue(simple_tic_tac_toe.check_win())

    def test_check_win_vertical(self):
        simple_tic_tac_toe.board[0][0] = 'X'
        simple_tic_tac_toe.board[1][0] = 'X'
        simple_tic_tac_toe.board[2][0] = 'X'
        self.assertTrue(simple_tic_tac_toe.check_win())

    def test_check_win_diagonal(self):
        simple_tic_tac_toe.board[0][0] = 'X'
        simple_tic_tac_toe.board[1][1] = 'X'
        simple_tic_tac_toe.board[2][2] = 'X'
        self.assertTrue(simple_tic_tac_toe.check_win())

if __name__ == '__main__':
    unittest.main()
