"""
This module contains the Player class.

"""
import pygame
from game.ship import Ship


class Player(Ship):
    # Player Magic Numbers
    STARTING_X = 1250 / 2
    STARTING_Y = 750 / 2

    def __int__(self):
        super().__init__(self.STARTING_X, self.STARTING_Y)

    def move(self, keys):
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
