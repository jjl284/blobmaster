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
        "L_inf": L_inf,
    }

def all_paths_2(blob):
    """Find all legal paths of length 2, sorted by slime amount"""
    paths = []
    for u in blob.tile.get_neighbors():
        if u and not u.blob:
            for v in u.get_neighbors():
                if v and not v.blob:
                    paths.append((blob, u, v, u.slime + v.slime))
    return sorted(paths, key=lambda p : p[3], reverse=True)


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

        blobmaster = self.player.blobmaster

        # Move blobmaster to thwart aggressive tactics
        paths = all_paths_2(blobmaster)
        if paths:
            blobmaster.move(paths[0][1])
            blobmaster.move(paths[0][2])

        # Move rest of blobs
        moves = []
        n_moves = 20
        for blob in [blobmaster] + self.player.blobs:
            if blob.size == 1:
                paths = all_paths_2(blob)
                if paths:
                    if paths[0][3] > 35 and n_moves > 0:
                        paths[0][0].move(paths[0][1])
                        paths[0][0].move(paths[0][2])
                        n_moves -= 1
                    else:
                        moves.append(paths[0])
        if n_moves > 0:
            moves.sort(key=lambda p: p[3], reverse=True)
            for m in moves[:n_moves]:
                m[0].move(m[1])
                m[0].move(m[2])

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
        """ If enemy has blob larger than 1x1, drop there
            Otherwise, drop adjacent to blobmaster (preference for squares that have an enemy blob, then neutral
        """
        blobmaster = self.player.blobmaster
        enemy_largest_slime = self.enemy_largest_slime()
        if enemy_largest_slime and enemy_largest_slime.size > 1:
            return enemy_largest_slime.tile

        tentative_drop = None
        for neighbour in blobmaster.tile.get_neighbors():
            if not tentative_drop:
                tentative_drop=neighbour
            if self.calculate_tile_value(neighbour) > self.calculate_tile_value(tentative_drop):
                tentative_drop=neighbour
        return tentative_drop

    def calculate_tile_value(self, tile):
        """ If enemy has blob larger than 1x1, drop there
            Otherwise, drop adjacent to blobmaster (preference for squares that have an enemy blob, then neutral

            Priority calculation = amount of slime
            + 15 if enemy blob is on
            + 10 if neutral blob

            TODO: other factors e.g. distance from blobmaster, locations of other slime, ability to capture
        """
        score = tile.slime
        if tile.blob and tile.blob.owner == self.player.opponent:
            score += 15
        elif tile.blob:
            score +=10
        return score

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
