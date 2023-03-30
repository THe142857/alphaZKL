import numpy as np


class Board:
    # 0 = empty, 1 = X, -1 = O
    def __init__(self, n=3):
        self.n = n
        self.board = np.zeros((n, n), np.int8)

    def valid_moves(self):
        np.where(self.board == 0)

    def move(self, move, p):
        self.board[move[0], move[1]] = p

    def has_won(self, p):
        # rows
        for i in range(self.n):
            if np.all(self.board[i] == p):
                return True

        # cols
        for i in range(self.n):
            if np.all(self.board[:][i] == p):
                return True

        # diag
        diag = self.board.diagonal()
        anti_diag = np.flip(self.board).diagonal()
        if diag == p:
            return True
        if anti_diag == p:
            return True

        return False

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
    b.move((2, 0), 1)
    print(b)
