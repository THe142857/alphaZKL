import numpy as np
from typing import List, Tuple


class Board:
    # 0 = empty, 1 = X, -1 = O
    def __init__(self, n=3):
        self.n = n
        self.board = np.zeros((n, n), np.int8)

    def valid_moves(self):
        np.where(self.board == 0)

    def move(self, move: Tuple[int, int], player: int):
        """Takes in a board position and a player and updates the board"""

        self.board[move[0], move[1]] = player

    def has_won(self, player: int):
        # rows
        for i in range(self.n):
            if np.all(self.board[i] == player):
                return True

        # cols
        for i in range(self.n):
            if np.all(self.board[:][i] == player):
                return True

        # diag
        diag = self.board.diagonal()
        anti_diag = np.flip(self.board).diagonal()

        return diag == player or anti_diag == player

    def __repr__(self):
        get_symbol = lambda x: "X" if x == 1 else "O" if x == -1 else " "
        res = ''
        for i in range(2 * self.n + 1):
            if i % 2 == 0:
                res += "――" * (2 * self.n - 1) + "\n"
            else:
                res += " | ".join([get_symbol(x) for x in self.board[i // 2]]) + "\n"
        return res


if __name__ == '__main__':
    b = Board()
    b.move((1, 1), 1)
    b.move((1, 2), -1)
    b.move((0, 0), -1)
    b.move((2, 1), 1)
    b.move((2, 0), -1)
    print(b)
