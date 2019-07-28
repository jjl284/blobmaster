# This is where you build your AI for the Blobmaster game.

from joueur.base_ai import BaseAI

# you can add additional import(s) here
import random
import math

def dist(tile_1, tile_2):
    x_dist = abs(tile_1.x - tile_2.x)
    y_dist = abs(tile_1.y - tile_2.y)
    manhattan = x_dist + y_dist
    L_inf = max(x_dist, y_dist)
    return {
        "x": x_dist,
        "y": y_dist,
        "sum": manhattan,
        "attack": manhattan == 0 and -99 or -manhattan,
        "L_inf": L_inf,
    }

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
        return "Team DJS"

    def run_turn(self):
        """ This is called every time it is this AI.player's turn.

        Returns:
            bool: Represents if you want to end your turn. True means end your turn, False means to keep your turn going and re-call this function.
        """

        if not self._target_blob or self._target_blob == self.player.blobmaster or self._target_blob.owner == self.player:
            if self.player.opponent.blobs:
                self._target_blob = random.choice(self.player.opponent.blobs)
            else:
                self._target_blob = self.player.blobmaster

        # Move blobmaster to thwart aggressive tactics
        blobmaster = self.player.blobmaster
        paths = self.all_paths_2(blobmaster, False)
        if paths:
            blobmaster.move(paths[0][1])
            blobmaster.move(paths[0][2])

        # Move rest of blobs
        for blob in self.player.blobs:
            if blob.size == 1:
                paths = self.all_paths_2(blob, int(blob.id) % 3 == 0)
                if paths and self.player.time_remaining > 2 * 10**9:
                    if paths[0][1]:
                        blob.move(paths[0][1])
                        if paths[0][2]:
                            blob.move(paths[0][2])

        dropzone = self.determine_drop_location()
        self.player.drop(dropzone)

        return True

    def enemy_largest_slime(self):
        """
            Returns enemy's largest blob (if tie, returns closest to our blobmaster)
        """
        blobmaster = self.player.blobmaster
        biggest_blob = None
        for blob in self.player.opponent.blobs:
            if not biggest_blob:
                biggest_blob=blob
            elif blob.size > biggest_blob.size:
                biggest_blob=blob
            # if two enemy blobs are same size, choose the closer one
            elif blob.size==biggest_blob.size and dist(blobmaster.tile,blob.tile)["sum"]<dist(blobmaster.tile,biggest_blob.tile)["sum"]:
                biggest_blob=blob
        return biggest_blob

    def determine_drop_location(self):
        """ If enemy has blob larger than 1x1, drop in the center
            Otherwise, drop adjacent to blobmaster (preference for squares that have an enemy blob, then neutral
        """
        blobmaster = self.player.blobmaster
        enemy_largest_slime = self.enemy_largest_slime()
        if enemy_largest_slime and enemy_largest_slime.size > 1:
            return self.get_blob_center_tile(enemy_largest_slime)

        neutral_blob_tiles = [blob.tile for blob in self.game.blobs if not blob.owner]

        tentative_drop = None
        for neighbour in blobmaster.tile.get_neighbors() + neutral_blob_tiles:
            if not tentative_drop:
                tentative_drop = neighbour
            if self.calculate_tile_value(neighbour) > self.calculate_tile_value(tentative_drop):
                tentative_drop = neighbour
        if tentative_drop.blob:
            return self.get_blob_center_tile(tentative_drop.blob)
        else:
            return tentative_drop

    def get_blob_center_tile(self, blob):
        center_tile = blob.tile
        dist_from_center = int(blob.size//2)
        return self.game.get_tile_at(center_tile.x + dist_from_center, center_tile.y + dist_from_center)


    def calculate_tile_value(self, tile):
        """ If enemy has blob larger than 1x1, drop there
            Otherwise, drop adjacent to blobmaster (preference for squares that have an enemy blob, then neutral

            Priority calculation = amount of slime
            + 15 if enemy blob is on
            + 10 if neutral blob

            TODO: other factors e.g. distance from blobmaster, locations of other slime, ability to capture
        """
        blobmaster = self.player.blobmaster
        score = tile.slime

        if tile.blob and tile.blob.owner == self.player.opponent:
            score += 15
        elif tile.blob and tile.blob.owner == None:
            score += 10
        elif tile.blob and tile.blob.owner == self.player and tile in blobmaster.tile.get_neighbors():
            # tile is own blob and adjacent to blobmaster
            score = -100
        return score

    def all_paths_2(self, blob, attack):
        """Find all legal paths of length 2, sorted by slime amount (or attack range)"""
        paths = []
        enemy_pos = self._target_blob.tile
        if attack:
            paths.append((blob, None, None, dist(blob.tile, enemy_pos)["attack"]))
        for u in blob.tile.get_neighbors():
            if attack:
                paths.append((blob, u, None, dist(u, enemy_pos)["attack"]))
            if u and not u.blob:
                for v in u.get_neighbors():
                    if v and not v.blob:
                        if attack:
                            paths.append((blob, u, v, dist(v, enemy_pos)["attack"]))
                        else:
                            paths.append((blob, u, v, u.slime + v.slime))
        return sorted(paths, key=lambda p : p[3], reverse=True)

    def get_neighboring_blob_tiles(self, blob):
        """ Return a list of tiles with neutral blobs.

        Empty list if no neutral blobs around.
        """
        neighboring_tiles = []
        top_left_coord = (blob.tile.x - 1, blob.tile.y -1)
        for i in [0, blob.size+2]:
            for j in range(blob.size+2):
                neighboring_tiles.append(self.game.get_tile_at(top_left_coord[0] + i, top_left_coord[1] + j))
                neighboring_tiles.append(self.game.get_tile_at(top_left_coord[0] + j, top_left_coord[1] + i))

        return [tile for tile in neighboring_tiles if tile]

    def get_neighboring_neutral_blob_tiles(self, blob):
        """ Return a list of tiles with neutral blobs.

        Empty list if no neutral blobs around.
        """
        return [tile for tile in self.get_neighboring_blob_tiles(blob) if tile.blob.owner is None]

    def get_neighboring_enemy_blob_tiles(self, blob):
        """ Return a list of tiles with enemy blobs.
        """
        return [tile for tile in self.get_neighboring_blob_tiles(blob) if tile.blob.owner == self.player.opponent]

    def start(self):
        """ This is called once the game starts and your AI knows its player and
            game. You can initialize your AI here.
        """
        # replace with your start logic
        self._target_blob = None

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
