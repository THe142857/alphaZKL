import numpy as np
from typing import List, Any
from agent import Agent, Policy, Value, Action


class Board:
    # 0 = empty, 1 = X, -1 = O
    def __init__(self, n: int = 3):
        self.n = n
        self.b = np.zeros((n, n), np.int8)

    def valid_moves(self):
        return np.where(self.b == 0)

    def move(self, move: Action, player: int):
        self.b[move[0], move[1]] = player

    def canonicalize(self, color: int):
        self.b *= color

    def has_won(self, color: int) -> bool:
        # rows
        for i in range(self.n):
            if np.all(self.b[i] == color):
                return True

        # cols
        for i in range(self.n):
            if np.all(self.b[:][i] == color):
                return True

        # diag
        diag = self.b.diagonal()
        anti_diag = np.flip(self.b).diagonal()

        return diag == color or anti_diag == color

    def __repr__(self) -> str:
        res = ""
        for i in range(2 * self.n + 1):
            if i % 2 == 0:
                res += "-" * (2 * self.n - 1) + "\n"
            else:
                res += "|".join(self.b[i // 2].astype(str)) + "\n"
        return res

    def __array__(self):
        return self.b


class Game:
    def __init__(self, n=3):
        self.n = n
        self.b = Board(n)

    def action_size(self) -> int:
        return self.n**2

    def is_done(self) -> bool:
        return self.b.valid_moves == ()

    def get_status(self, agent: Agent) -> int:
        if self.b.has_won(agent.num):
            return 1
        if self.b.has_won(-agent.num):
            return -1
        return 0

    def canonicalize(self, agent: Agent):
        self.b.canonicalize(agent.num)

    def step(self, agent: Agent, action: Action):
        self.b.move(action, agent.num)

    def get_symmetries(self, pi: Policy) -> List[Any]:
        pi_b = np.reshape(pi[:-1], (self.n, self.n))
        sym = []

        for i in range(1, 5):
            for j in [True, False]:
                newB = np.rot90(self.b, i)
                newPi = np.rot90(pi_b, i)
                if j:
                    newB = np.fliplr(newB)
                    newPi = np.fliplr(newPi)
                sym += [(newB, list(newPi.ravel()) + [pi[-1]])]
        return sym


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
