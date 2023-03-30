import numpy as np


class Board:
    # 0 = empty, 1 = X, -1 = O
    def __init__(self, n=3):
        self.n = n
        self.board = np.zeros((n, n))

    def valid_moves(self):
        np.where(self.board == 0)

    def move(self, move, color):
        self.board[move[0], move[1]] = color

    def winner(self):
        # rows
        for i in range(self.n):
            if np.all(self.board[i] == self.board[i][0]):
                return self.board[i][0]

        # cols
        for i in range(self.n):
            if np.all(self.board[:][i] == self.board[0][i]):
                return self.board[0][i]

        # diag
        diag = self.board.diagonal()
        anti_diag = np.flip(self.board).diagonal()
        if diag == diag[0]:
            return diag[0]
        if anti_diag == anti_diag[0]:
            return diag[0]

        return 0
