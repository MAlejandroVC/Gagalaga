"""
This module contains the Enemy class.
The Enemy class extends the Ship class.
"""
import pygame
from game.ship import Ship
from game import settings


class Enemy(Ship):
    """
    Enemy class.
    Extends the Ship class.
    """

    # Shape Magic Numbers
    VERTICES = [(0, 0), (settings.SHIP_WIDTH / 2, settings.SHIP_HEIGHT), (settings.SHIP_WIDTH, 0)]
    COLOR = (0, 0, 255, 0)

    # Ship Image
    ENEMY_IMAGE = pygame.image.load('assets/Enemy/Ship.png')

    def __init__(self, starting_x: int, starting_y: int):
        super().__init__(starting_x, starting_y, self.VERTICES, self.COLOR)

    def draw(self, screen: pygame.Surface) -> None:
        """
        Draws the enemy.
        :param screen: screen object to draw on.
        :return: None
        """
        adjusted_x = self.body.position.x - settings.SHIP_WIDTH * .5
        adjusted_y = self.body.position.y - settings.SHIP_HEIGHT * .5
        super().draw(screen, self.ENEMY_IMAGE, adjusted_x, adjusted_y)

    def move(self) -> None:
        """
        If the ship is on an even file, it moves to the right.
        If the ship is on an odd file, it moves to the left.
        Once it reaches the end of the screen, it moves down one file.

        Uses Ship.move() to move the ship.
        :return: None
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
