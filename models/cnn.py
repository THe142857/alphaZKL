# ==========[ IMPORTS ]==========
import pytorch_lightning as pl
from tensorflow.keras.models import *
from tensorflow.keras.layers import *
from tensorflow.keras.optimizers import *


# ==========[ CNN ]==========
class CNN():

    def __init__(self, game, args):
        """Takes as input a board and outputs:

        - pi (probability distribution over moves)
        - v (estimated value for the board)
        """

        # Game configuration
        self.x, self.y = game.board_size()
        self.action_size = game.action_size()

        # Hyperparameters
        self.num_channels = 512
        self.dropout = 0.3
        self.lr = 0.001


        # Input (n, x, y) where n is the batch_size
        self.input_boards = Input(shape=(self.x, self.y))

        # Add a dimension to the input to represent the number of channels (n, x,  y, 1)
        board = Reshape((self.x, self.y, 1))(self.input_boards)

        # Convolutional layers
        conv1 = Activation('relu')(BatchNormalization(axis=3)(Conv2D(self.num_channels, 3, padding='same')(board)))
        conv2 = Activation('relu')(BatchNormalization(axis=3)(Conv2D(self.num_channels, 3, padding='same')(conv1)))
        conv3 = Activation('relu')(BatchNormalization(axis=3)(Conv2D(self.num_channels, 3, padding='same')(conv2)))
        conv4 = Activation('relu')(BatchNormalization(axis=3)(Conv2D(self.num_channels, 3, padding='valid')(conv3)))
        flat = Flatten()(conv4)       
        
        # Fully connected layers
        fc1 = Dropout(self.dropout)(Activation('relu')(BatchNormalization(axis=1)(Dense(1024)(flat))))
        fc2 = Dropout(self.dropout)(Activation('relu')(BatchNormalization(axis=1)(Dense(512)(fc1))))
        
        # Output layers
        self.pi = Dense(self.action_size, activation='softmax', name='pi')(fc2)
        self.v = Dense(1, activation='tanh', name='v')(fc2)                    

        # Compile model
        self.model = Model(inputs=self.input_boards, outputs=[self.pi, self.v])
        self.model.compile(loss=['categorical_crossentropy','mean_squared_error'], optimizer=Adam(self.lr))