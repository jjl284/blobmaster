# This is where you build your AI for the Blobmaster game.

from joueur.base_ai import BaseAI

# you can add additional import(s) here
import random

class AI(BaseAI):
    """ The AI you add and improve code inside to play Blobmaster. """

    @property
    def game(self):
        """The reference to the Game instance this AI is playing.

        :rtype: games.blobmaster.game.Game
        """
        return self._game # don't directly touch this "private" variable pls

    @property
    def player(self):
        """The reference to the Player this AI controls in the Game.

        :rtype: games.blobmaster.player.Player
        """
        return self._player # don't directly touch this "private" variable pls

    def get_name(self):
        """ This is the name you send to the server so your AI will control the
            player named this string.

        Returns
            str: The name of your Player.
        """
        return "Blobmaster Python Player" # REPLACE THIS WITH YOUR TEAM NAME

    def run_turn(self):
        """ This is called every time it is this AI.player's turn.

        Returns:
            bool: Represents if you want to end your turn. True means end your turn, False means to keep your turn going and re-call this function.
        """
        # This is a basic AI that moves its blobmaster around and drops blobs randomly
        # Replace this code with your own!

        blobmaster = self.player.blobmaster
        neighbors = blobmaster.tile.get_neighbors()
        blobmaster.move(random.choice(neighbors))

        dropzone = random.choice(self.game.tiles)
        self.player.drop(dropzone)

        return True

    def start(self):
        """ This is called once the game starts and your AI knows its player and
            game. You can initialize your AI here.
        """
        # replace with your start logic

    def game_updated(self):
        """ This is called every time the game's state updates, so if you are
        tracking anything you can update it here.
        """
        # replace with your game updated logic

    def end(self, won, reason):
        """ This is called when the game ends, you can clean up your data and
            dump files here if need be.

        Args:
            won (bool): True means you won, False means you lost.
            reason (str): The human readable string explaining why your AI won
            or lost.
        """
        # replace with your end logic
