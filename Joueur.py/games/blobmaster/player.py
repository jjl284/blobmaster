# Player: A player in this game. Every AI controls one player.

# DO NOT MODIFY THIS FILE
# Never try to directly create an instance of this class, or modify its member variables.
# Instead, you should only be reading its variables and calling its functions.

from games.blobmaster.game_object import GameObject

# <<-- Creer-Merge: imports -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
# you can add additional import(s) here
# <<-- /Creer-Merge: imports -->>

class Player(GameObject):
    """The class representing the Player in the Blobmaster game.

    A player in this game. Every AI controls one player.
    """

    def __init__(self):
        """Initializes a Player with basic logic as provided by the Creer code generator."""
        GameObject.__init__(self)

        # private attributes to hold the properties so they appear read only
        self._blobmaster = None
        self._blobs = []
        self._client_type = ""
        self._drops = []
        self._drops_left = 0
        self._lost = False
        self._name = "Anonymous"
        self._opponent = None
        self._reason_lost = ""
        self._reason_won = ""
        self._score = 0
        self._slime = 0
        self._time_remaining = 0
        self._won = False

    @property
    def blobmaster(self):
        """The Blobmaster owned by this Player.

        :rtype: games.blobmaster.blob.Blob
        """
        return self._blobmaster

    @property
    def blobs(self):
        """Every Blob owned by this Player.

        :rtype: list[games.blobmaster.blob.Blob]
        """
        return self._blobs

    @property
    def client_type(self):
        """What type of client this is, e.g. 'Python', 'JavaScript', or some other language. For potential data mining purposes.

        :rtype: str
        """
        return self._client_type

    @property
    def drops(self):
        """Tiles which future blobs will drop onto, this determines the order in which simultaneous drops are handled.

        :rtype: list[games.blobmaster.tile.Tile]
        """
        return self._drops

    @property
    def drops_left(self):
        """How many more Blobs this Player can drop this turn.

        :rtype: int
        """
        return self._drops_left

    @property
    def lost(self):
        """If the player lost the game or not.

        :rtype: bool
        """
        return self._lost

    @property
    def name(self):
        """The name of the player.

        :rtype: str
        """
        return self._name

    @property
    def opponent(self):
        """This player's opponent in the game.

        :rtype: games.blobmaster.player.Player
        """
        return self._opponent

    @property
    def reason_lost(self):
        """The reason why the player lost the game.

        :rtype: str
        """
        return self._reason_lost

    @property
    def reason_won(self):
        """The reason why the player won the game.

        :rtype: str
        """
        return self._reason_won

    @property
    def score(self):
        """How many points this player has.

        :rtype: int
        """
        return self._score

    @property
    def slime(self):
        """How much slime this player has.

        :rtype: int
        """
        return self._slime

    @property
    def time_remaining(self):
        """The amount of time (in ns) remaining for this AI to send commands.

        :rtype: float
        """
        return self._time_remaining

    @property
    def won(self):
        """If the player won the game or not.

        :rtype: bool
        """
        return self._won

    def drop(self, tile):
        """ Spawns a Blob in the air above the given tile.

        Args:
            tile (games.blobmaster.tile.Tile): The Tile to spawn a Blob on.

        Returns:
            bool: True if the drop worked, False otherwise.
        """
        return self._run_on_server('drop', tile=tile)



    # <<-- Creer-Merge: functions -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
    # if you want to add any client side logic (such as state checking functions) this is where you can add them
    # <<-- /Creer-Merge: functions -->>
