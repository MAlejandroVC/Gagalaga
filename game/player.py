"""
This module contains the Player class.
The Player class extends the Ship class.
"""
import pygame
from game.ship import Ship
from game.singleton import *
from game.projectile import Projectile


class Player(Ship):
    """
    Player class.
    Extends the Ship class.
    """

    # Shape Magic Numbers
    VERTICES = [(0, 0), (-settings.SHIP_WIDTH / 2, -settings.SHIP_HEIGHT), (-settings.SHIP_WIDTH, 0)]
    COLOR = (0, 255, 0, 0)

    # Coordinates
    STARTING_X = settings.SCREEN_WIDTH / 2
    STARTING_Y = settings.SCREEN_HEIGHT - settings.SHIP_HEIGHT - settings.PADDING

    # Ship Image
    PLAYER_IMAGE = pygame.image.load('assets/Player/Ship.png')

    def __init__(self, starting_x: int, starting_y: int):
        super().__init__(starting_x, starting_y, self.VERTICES, self.COLOR)

    def draw(self, screen: pygame.Surface) -> None:
        """
        Draws the player.
        :param screen: screen object to draw on.
        :return: None
        """
        adjusted_x = self.body.position.x - settings.SHIP_WIDTH*1.5
        adjusted_y = self.body.position.y - settings.SHIP_HEIGHT*1.5
        super().draw(screen, self.PLAYER_IMAGE, adjusted_x, adjusted_y)

    def player_key(self, keys: pygame.key.ScancodeWrapper) -> None:
        """
        Moves the player in a given thrust_direction depending on the keys pressed.
        Also shoots if the space bar is pressed.
        :param keys: keys pressed.
        :return: None
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
                super().shoot(Projectile.SHOOT_UP)
        else:
            super().move(Ship.THRUST_NONE)
