# Blob: A Blob.  Can move and collect slime.

# DO NOT MODIFY THIS FILE
# Never try to directly create an instance of this class, or modify its member variables.
# Instead, you should only be reading its variables and calling its functions.

from games.blobmaster.game_object import GameObject

# <<-- Creer-Merge: imports -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
# you can add additional import(s) here
# <<-- /Creer-Merge: imports -->>

class Blob(GameObject):
    """The class representing the Blob in the Blobmaster game.

    A Blob.  Can move and collect slime.
    """

    def __init__(self):
        """Initializes a Blob with basic logic as provided by the Creer code generator."""
        GameObject.__init__(self)

        # private attributes to hold the properties so they appear read only
        self._is_blobmaster = False
        self._is_dead = False
        self._moves_left = 0
        self._owner = None
        self._size = 0
        self._tile = None

    @property
    def is_blobmaster(self):
        """Whether this Blob is a Blobmaster.

        :rtype: bool
        """
        return self._is_blobmaster

    @property
    def is_dead(self):
        """Whether this Blob is dead and has been removed from the game.

        :rtype: bool
        """
        return self._is_dead

    @property
    def moves_left(self):
        """How many more moves this Blob can do this turn.

        :rtype: int
        """
        return self._moves_left

    @property
    def owner(self):
        """The Player that owns and can control this Blob, or None if this is a neutral blob.

        :rtype: games.blobmaster.player.Player
        """
        return self._owner

    @property
    def size(self):
        """The width and height of this Blob.

        :rtype: int
        """
        return self._size

    @property
    def tile(self):
        """The top-left (smallest x,y) Tile that this Blob occupies.

        :rtype: games.blobmaster.tile.Tile
        """
        return self._tile

    def move(self, tile):
        """ Moves this Blob onto the given tile.

        Args:
            tile (games.blobmaster.tile.Tile): The tile for this Blob to move onto.

        Returns:
            bool: True if the move worked, False otherwise.
        """
        return self._run_on_server('move', tile=tile)

    # <<-- Creer-Merge: functions -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
    # if you want to add any client side logic (such as state checking functions) this is where you can add them
    # <<-- /Creer-Merge: functions -->>
