"""
This module contains the Player class.

"""
import pygame
from game.ship import Ship
from game import settings


class Player(Ship):
    """
    Player class.
    Extends the Ship class.
    """

    # Player Magic Numbers
    STARTING_X = settings.SCREEN_WIDTH / 2
    STARTING_Y = settings.SCREEN_HEIGHT - Ship.SHIP_HEIGHT - settings.PADDING

    def __int__(self):
        super().__init__(self.STARTING_X, self.STARTING_Y)

    def move(self, keys):
        """
        Moves the player in a given direction depending on the keys pressed.
        Also shoots if the space bar is pressed.
        :param keys: keys pressed.
        """
        if keys[pygame.K_w]:
            super().move('up')
        if keys[pygame.K_s]:
            super().move('down')
        if keys[pygame.K_a]:
            super().move('left')
        if keys[pygame.K_d]:
            super().move('right')
        if keys[pygame.K_SPACE]:
            super().shoot()
