# ==========[ IMPORTS ]==========
from game import Game
from agent import Agent
from mcts import MCTS
from typing import List, Tuple
import numpy as np


# ==========[ SELF-PLAY ]==========
class SelfPlay():

    def __init__(self, game: Game, agent: Agent):
        """Runs self-play episodes and learns from them.

        :param game: The game being played
        :type game: Game
        :param agent: The agent playing the game
        :type agent: Agent
        """

        self.game = game
        self.agent = agent
        self.opponent = Agent(game)


    def run_episode(self) -> List[Tuple[np.ndarray, int, np.ndarray, int]]:
        """
        Runs one episode starting with player one.
        - pi is the MCTS-informed policy vector 
        - v is +1 for a win, 0 for a draw, -1 for a loss.

        :return: List of examples of the form (canonical_board, current_player, pi, v)
        :rtype: List[Tuple[np.ndarray, int, np.ndarray, int]]
        """

        # Initialize the game
        board = self.game.initialize_board()
        examples = []
        step = 0
        current_player = 1

        # Step through game
        while True:
            step += 1

            # Compute action probabilities
            canonical_board = self.game.canonicalize(board, current_player)
            pi = self.agent.get_policy(canonical_board)

            # Create example and add symmetries
            symmetries = self.game.get_symmetries(canonical_board, pi)
            for board, player in symmetries:
                examples.append((board, player, pi, None))

            # Take action and step game
            action = np.random.choice(len(pi), p=pi)
            board, current_player = self.game.step(board, current_player, action)

            # TODO: Check if game is over and assign rewards
            pass

    def learn(self):
        pass