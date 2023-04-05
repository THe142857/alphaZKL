from tictactoe import Game
import lightning.pytorch as pl

class TicTacToeNN(pl.LightningModule):
    def __init__(self, game: Game):
        super().__init__()
        self.x, self.y = game.board_size()
        self.action_size = game.action_size()
