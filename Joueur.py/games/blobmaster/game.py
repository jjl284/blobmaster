# Game: Move around to collect slime and cover the battlefield with ever-bigger blobs to win.

# DO NOT MODIFY THIS FILE
# Never try to directly create an instance of this class, or modify its member variables.
# Instead, you should only be reading its variables and calling its functions.

from joueur.base_game import BaseGame

# import game objects
from games.blobmaster.blob import Blob
from games.blobmaster.game_object import GameObject
from games.blobmaster.player import Player
from games.blobmaster.tile import Tile

# <<-- Creer-Merge: imports -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
# you can add additional import(s) here
# <<-- /Creer-Merge: imports -->>

class Game(BaseGame):
    """The class representing the Game in the Blobmaster game.

    Move around to collect slime and cover the battlefield with ever-bigger blobs to win.
    """

    def __init__(self):
        """Initializes a Game with basic logic as provided by the Creer code generator."""
        BaseGame.__init__(self)

        # private attributes to hold the properties so they appear read only
        self._big_blob_speed = 0
        self._blob_cost_exponent = 0
        self._blob_cost_multiplier = 0
        self._blobmasters = []
        self._blobs = []
        self._bonus_slime_for_fewer_blobs = 0
        self._current_player = None
        self._current_turn = 0
        self._death_slime = 0
        self._game_objects = {}
        self._map_height = 0
        self._map_width = 0
        self._max_drops_per_turn = 0
        self._max_player_slime = 0
        self._max_slime_spawned_on_tile = 0
        self._max_starting_walls = 0
        self._max_turns = 100
        self._min_starting_walls = 0
        self._per_tile_drop_delay = 0
        self._players = []
        self._points_to_win = 0
        self._session = ""
        self._slime_spawn_rate = 0
        self._small_blob_speed = 0
        self._tiles = []
        self._tiles_covered_to_win = 0
        self._time_added_per_turn = 0

        self.name = "Blobmaster"

        self._game_object_classes = {
            'Blob': Blob,
            'GameObject': GameObject,
            'Player': Player,
            'Tile': Tile
        }

    @property
    def big_blob_speed(self):
        """Blobs of size > 1 can move this many tiles per turn.

        :rtype: int
        """
        return self._big_blob_speed

    @property
    def blob_cost_exponent(self):
        """The E in the blob cost formula Mx**E.

        :rtype: float
        """
        return self._blob_cost_exponent

    @property
    def blob_cost_multiplier(self):
        """The M in the blob cost formula Mx**E.

        :rtype: float
        """
        return self._blob_cost_multiplier

    @property
    def blobmasters(self):
        """Every Blobmaster in the game.

        :rtype: list[games.blobmaster.blob.Blob]
        """
        return self._blobmasters

    @property
    def blobs(self):
        """Every Blob in the game.

        :rtype: list[games.blobmaster.blob.Blob]
        """
        return self._blobs

    @property
    def bonus_slime_for_fewer_blobs(self):
        """The player with fewer blobs is given this much slime per less blobs every turn.

        :rtype: int
        """
        return self._bonus_slime_for_fewer_blobs

    @property
    def current_player(self):
        """The player whose turn it is currently. That player can send commands. Other players cannot.

        :rtype: games.blobmaster.player.Player
        """
        return self._current_player

    @property
    def current_turn(self):
        """The current turn number, starting at 0 for the first player's turn.

        :rtype: int
        """
        return self._current_turn

    @property
    def death_slime(self):
        """The amount of slime added to a blob's tiles when it dies.

        :rtype: int
        """
        return self._death_slime

    @property
    def game_objects(self):
        """A mapping of every game object's ID to the actual game object. Primarily used by the server and client to easily refer to the game objects via ID.

        :rtype: dict[str, games.blobmaster.game_object.GameObject]
        """
        return self._game_objects

    @property
    def map_height(self):
        """The number of Tiles in the map along the y (vertical) axis.

        :rtype: int
        """
        return self._map_height

    @property
    def map_width(self):
        """The number of Tiles in the map along the x (horizontal) axis.

        :rtype: int
        """
        return self._map_width

    @property
    def max_drops_per_turn(self):
        """A Player can drop at most this many blobs per turn.

        :rtype: int
        """
        return self._max_drops_per_turn

    @property
    def max_player_slime(self):
        """The maximum amount of slime a player can hold at any one time.

        :rtype: int
        """
        return self._max_player_slime

    @property
    def max_slime_spawned_on_tile(self):
        """No more slime will spawn on a tile with at least this much slime already on it.

        :rtype: int
        """
        return self._max_slime_spawned_on_tile

    @property
    def max_starting_walls(self):
        """The maximum number of neutral blobs spawned at the start of the match.

        :rtype: int
        """
        return self._max_starting_walls

    @property
    def max_turns(self):
        """The maximum number of turns before the game will automatically end.

        :rtype: int
        """
        return self._max_turns

    @property
    def min_starting_walls(self):
        """The minimum number of neutral blobs spawned at the start of the match.

        :rtype: int
        """
        return self._min_starting_walls

    @property
    def per_tile_drop_delay(self):
        """It takes the ceiling of this many turns times the number tiles away from your blobmaster to drop a blob onto a tile.

        :rtype: float
        """
        return self._per_tile_drop_delay

    @property
    def players(self):
        """List of all the players in the game.

        :rtype: list[games.blobmaster.player.Player]
        """
        return self._players

    @property
    def points_to_win(self):
        """A player wins if they can reach this many cumulative tiles covered.

        :rtype: int
        """
        return self._points_to_win

    @property
    def session(self):
        """A unique identifier for the game instance that is being played.

        :rtype: str
        """
        return self._session

    @property
    def slime_spawn_rate(self):
        """This much slime is added to every empty tile every turn.

        :rtype: int
        """
        return self._slime_spawn_rate

    @property
    def small_blob_speed(self):
        """1x1 blobs can move this many tiles per turn.

        :rtype: int
        """
        return self._small_blob_speed

    @property
    def tiles(self):
        """All the tiles in the map, stored in Row-major order. Use `x + y * mapWidth` to access the correct index.

        :rtype: list[games.blobmaster.tile.Tile]
        """
        return self._tiles

    @property
    def tiles_covered_to_win(self):
        """A player wins if they can cover this many tiles with their blobs on a single turn.

        :rtype: int
        """
        return self._tiles_covered_to_win

    @property
    def time_added_per_turn(self):
        """The amount of time (in nano-seconds) added after each player performs a turn.

        :rtype: int
        """
        return self._time_added_per_turn


    def get_tile_at(self, x, y):
        """Gets the Tile at a specified (x, y) position
        Args:
            x (int): integer between 0 and the map_width
            y (int): integer between 0 and the map_height
        Returns:
            games.blobmaster.tile.Tile: the Tile at (x, y) or None if out of bounds
        """
        if x < 0 or y < 0 or x >= self.map_width or y >= self.map_height:
            # out of bounds
            return None

        return self.tiles[x + y * self.map_width]

    # <<-- Creer-Merge: functions -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
    # if you want to add any client side logic (such as state checking functions) this is where you can add them
    # <<-- /Creer-Merge: functions -->>
