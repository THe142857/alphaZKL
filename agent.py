from tictactoe import Game
from agent import Agent
from typing import List, Tuple
import numpy as np

Policy = np.ndarray
Value = float
Action = Tuple[int, int]


class Agent:
    """
    Does not consider the current player, only deals with the canonical form of the board.
    """

    def __init__(self, game: Game, num: int):
        # use -1 for one player and 1 for other
        self.game = game
        self.num = num
        pass

    def train(self, examples: List[Tuple[np.ndarray, np.ndarray, float]]):
        """
        This function trains the neural network with examples obtained from
        self-play.

        Input:
            examples: a list of training examples, where each example is of form
                      (board, pi, v). pi is the MCTS informed policy vector for
                      the given board, and v is its value. The examples has
                      board in its canonical form.
        """
        pass

    def predict(self, board: np.ndarray) -> Tuple[Policy, Value]:
        """
        Input:
            board: current board in its canonical form.

        Returns:
            pi: a policy vector for the current board- a numpy array of length
                game.getActionSize
            v: a float in [-1,1] that gives the value of the current board
        """
        pass

    def save_checkpoint(self, folder: str, filename: str):
        """
        Saves the current neural network (with its parameters) in
        folder/filename
        """
        pass

    def load_checkpoint(self, folder: str, filename: str):
        """
        Loads parameters of the neural network from folder/filename
        """
        pass
