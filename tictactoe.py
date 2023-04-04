import numpy as np
from typing import Tuple


class Board:
    # 0 = empty, 1 = X, -1 = O
    def __init__(self, n: int = 3):
        self.n = n
        self.board = np.zeros((n, n), np.int8)

    def valid_moves(self):
        np.where(self.board == 0)

    def move(self, move: Tuple[int, int], player: int):

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
        res = ""
        for i in range(2 * self.n + 1):
            if i % 2 == 0:
                res += "-" * (2 * self.n - 1) + "\n"
            else:
                res += "|".join(self.board[i // 2].astype(str)) + "\n"
        return res


if __name__ == "__main__":
    b = Board()
    p = 1
    while True:
        x, y = input().split(" ")
        b.move((int(x), int(y)), p)
        print(b)
        if b.has_won(p):
            print(f"{p} has won")
            break
        p = 2 if p == 1 else 1