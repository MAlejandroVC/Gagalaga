"""
This module contains the Player class.

"""
import pygame
from game.ship import Ship
from game import settings
from game.singleton import *


class Player(Ship):
    """
    Player class.
    Extends the Ship class.
    """

    # Shape Magic Numbers
    VERTICES = [(0, 0), (-settings.SHIP_WIDTH / 2, -settings.SHIP_HEIGHT), (-settings.SHIP_WIDTH, 0)]
    COLOR = (0, 0, 0, 0)

    # Coordinates
    STARTING_X = settings.SCREEN_WIDTH / 2
    STARTING_Y = settings.SCREEN_HEIGHT - settings.SHIP_HEIGHT - settings.PADDING

    # Ship Image
    PLAYER_IMAGE = pygame.image.load('assets/Player/Ship.png')

    __screen = ScreenSingleton(settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT)

    def __int__(self):
        super().__init__(self.STARTING_X, self.STARTING_Y)

    def draw(self):
        """
        Draws the ship on the screen.
        """
        scaled_player_image = pygame.transform.scale(self.PLAYER_IMAGE, (settings.SHIP_WIDTH*2, settings.SHIP_HEIGHT*2))
        adjusted_position = (self.body.position.x - settings.SHIP_WIDTH*1.5,
                             self.body.position.y - settings.SHIP_HEIGHT*1.5)

        self.__screen.screen.blit(scaled_player_image, adjusted_position)

    def player_key(self, keys):
        """
        Moves the player in a given thrust_direction depending on the keys pressed.
        Also shoots if the space bar is pressed.
        :param keys: keys pressed.
        """
        if keys[pygame.K_w] or keys[pygame.K_s] or keys[pygame.K_a] or keys[pygame.K_d] or keys[pygame.K_SPACE]:
            if keys[pygame.K_w]:
                pass  # super().move(Ship.THRUST_UP)
            if keys[pygame.K_s]:
                pass  # super().move(Ship.THRUST_DOWN)
            if keys[pygame.K_a]:
                super().move(Ship.THRUST_LEFT)
            if keys[pygame.K_d]:
                super().move(Ship.THRUST_RIGHT)
            if keys[pygame.K_SPACE]:
                super().shoot('up')
        else:
            super().move(Ship.THRUST_NONE)
