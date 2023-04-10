"""
This module contains the Enemy class.

"""
import pygame
from game.ship import Ship
from game import settings
from game.singleton import *


class Enemy(Ship):
    """
    Enemy class.
    Extends the Ship class.
    """

    # Shape Magic Numbers
    VERTICES = [(0, 0), (settings.SHIP_WIDTH / 2, settings.SHIP_HEIGHT), (settings.SHIP_WIDTH, 0)]
    COLOR = (0, 0, 0, 0)

    # Ship Image
    PLAYER_IMAGE = pygame.image.load('assets/Enemy/Ship.png')

    __screen = ScreenSingleton(settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT)

    def __int__(self, starting_x, starting_y):
        super().__init__(starting_x, starting_y)

    def move(self):
        """
        If the ship is on an even file, it moves to the right.
        If the ship is on an odd file, it moves to the left.
        Once it reaches the end of the screen, it moves down one file.

        Uses Ship.move() to move the ship.
        """
        if settings.is_even_file(self.body.position.y):
            if self.body.position.x >= settings.SCREEN_WIDTH - settings.PADDING - settings.SHIP_WIDTH:
                super().move(Ship.THRUST_DOWN)
            else:
                super().move(Ship.THRUST_RIGHT)
        if settings.is_odd_file(self.body.position.y):
            if self.body.position.x <= settings.PADDING + settings.SHIP_WIDTH:
                super().move(Ship.THRUST_DOWN)
            else:
                super().move(Ship.THRUST_LEFT)

    def draw(self):
        """
        Draws the ship on the screen.
        """
        scaled_player_image = pygame.transform.scale(self.PLAYER_IMAGE, (settings.SHIP_WIDTH*2, settings.SHIP_HEIGHT*2))
        adjusted_position = (self.body.position.x - settings.SHIP_WIDTH*.5,
                             self.body.position.y - settings.SHIP_HEIGHT*.5)

        self.__screen.screen.blit(scaled_player_image, adjusted_position)
