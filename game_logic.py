import random

class TicTacToeGame:
    def __init__(self, size=3):
        self.size = size
        self.board = [[' ' for _ in range(size)] for _ in range(size)]
        self.current_player = 'X'

    def make_move(self, row, col):
        if 0 <= row < self.size and 0 <= col < self.size and self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            return True
        return False

    def check_win(self, player):
        win_condition = 5 if self.size == 5 else 3

        # Check horizontal
        for r in range(self.size):
            for c in range(self.size - win_condition + 1):
                if all(self.board[r][c+i] == player for i in range(win_condition)):
                    return True

        # Check vertical
        for c in range(self.size):
            for r in range(self.size - win_condition + 1):
                if all(self.board[r+i][c] == player for i in range(win_condition)):
                    return True

        # Check diagonal (top-left to bottom-right)
        for r in range(self.size - win_condition + 1):
            for c in range(self.size - win_condition + 1):
                if all(self.board[r+i][c+i] == player for i in range(win_condition)):
                    return True

        # Check anti-diagonal (top-right to bottom-left)
        for r in range(self.size - win_condition + 1):
            for c in range(win_condition - 1, self.size):
                if all(self.board[r+i][c-i] == player for i in range(win_condition)):
                    return True
        return False

    def is_full(self):
        return all(cell != ' ' for row in self.board for cell in row)

    def get_empty_cells(self):
        return [(r, c) for r in range(self.size) for c in range(self.size) if self.board[r][c] == ' ']

    def _get_easy_move(self):
        return random.choice(self.get_empty_cells())

    def _get_medium_move(self):
        computer_player = self.current_player
        human_player = 'O' if computer_player == 'X' else 'X'

        # 1. Win if possible
        for r, c in self.get_empty_cells():
            self.board[r][c] = computer_player
            if self.check_win(computer_player):
                self.board[r][c] = ' '
                return r, c
            self.board[r][c] = ' '

        # 2. Block if necessary
        for r, c in self.get_empty_cells():
            self.board[r][c] = human_player
            if self.check_win(human_player):
                self.board[r][c] = ' '
                return r, c
            self.board[r][c] = ' '

        # 3. Otherwise, random move
        return self._get_easy_move()

    def _minimax(self, maximizing_player, computer_player, human_player):
        if self.check_win(computer_player):
            return 1
        if self.check_win(human_player):
            return -1
        if self.is_full():
            return 0

        if maximizing_player:
            best_score = -float('inf')
            player_to_move = computer_player
            for r, c in self.get_empty_cells():
                self.board[r][c] = player_to_move
                score = self._minimax(False, computer_player, human_player)
                self.board[r][c] = ' '
                best_score = max(score, best_score)
            return best_score
        else:  # Minimizing player
            best_score = float('inf')
            player_to_move = human_player
            for r, c in self.get_empty_cells():
                self.board[r][c] = player_to_move
                score = self._minimax(True, computer_player, human_player)
                self.board[r][c] = ' '
                best_score = min(score, best_score)
            return best_score

    def _get_hard_move(self):
        best_score = -float('inf')
        best_move = None
        computer_player = self.current_player
        human_player = 'O' if computer_player == 'X' else 'X'

        for r, c in self.get_empty_cells():
            self.board[r][c] = computer_player
            score = self._minimax(False, computer_player, human_player)
            self.board[r][c] = ' '
            if score > best_score:
                best_score = score
                best_move = (r, c)

        return best_move if best_move else self._get_easy_move()

    def get_computer_move(self, difficulty):
        if not self.get_empty_cells():
            return None

        if difficulty == 'easy':
            return self._get_easy_move()
        elif difficulty == 'medium':
            return self._get_medium_move()
        elif difficulty == 'hard':
            if self.size >= 4:
                return self._get_medium_move()
            return self._get_hard_move()

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def reset_game(self):
        self.board = [[' ' for _ in range(self.size)] for _ in range(self.size)]
        self.current_player = 'X'
