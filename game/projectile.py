"""
This module contains the Projectile interface and its concrete implementations.
Concrete implementations are: Bullet, Rocket, and Laser.
"""

import pygame
import pymunk
from abc import ABC
from game.singleton import SpaceSingleton


class Projectile(ABC):
    """
    Projectile interface.
    """
    # Projectile Magic Numbers
    PROJECTILE_MASS = 1
    PROJECTILE_RADIUS = 5
    PROJECTILE_MOMENT = pymunk.moment_for_circle(PROJECTILE_MASS, 0, PROJECTILE_RADIUS)
    PROJECTILE_ELASTICITY = 0
    PROJECTILE_FRICTION = 1

    # Projectile Movement Magic Numbers
    IMPULSE_CONSTANT = 1000
    SHOOT_UP = (0, -1 * IMPULSE_CONSTANT)
    SHOOT_DOWN = (0, 1 * IMPULSE_CONSTANT)
    CENTER_OF_GRAVITY = (0, 0)

    def __init__(self, x: int, y: int, direction: tuple[int, int]):
        self.body = None
        self.shape = None
        self.space = SpaceSingleton()
        self.destroyed = False

        self.body = pymunk.Body(self.PROJECTILE_MASS, self.PROJECTILE_MOMENT)
        self.body.position = x, y
        self.shape = pymunk.Circle(self.body, self.PROJECTILE_RADIUS)
        self.shape.elasticity = self.PROJECTILE_ELASTICITY
        self.shape.friction = self.PROJECTILE_FRICTION
        self.body.apply_impulse_at_local_point(direction, self.CENTER_OF_GRAVITY)
        self.shape.color = pygame.color.THECOLORS['white']
        self.space.add(self.body, self.shape)
        self.shape.belonging_object = self

    def draw(self, screen: pygame.Surface) -> None:
        """
        Draws the projectile.
        :param screen: screen to draw on.
        :return: None
        """
        pass

    def destroy(self) -> None:
        """
        Destroys the projectile.
        :return: None
        """
        self.destroyed = True


class Bullet(Projectile):
    """
    Bullet class.
    """
    def __init__(self, x: int, y: int, direction: tuple[int, int]):
        super().__init__(x, y, direction)
        self.shape.color = pygame.color.THECOLORS['blue']


class Rocket(Projectile):
    """
    Bullet class.
    """
    def __init__(self, x: int, y: int, direction: tuple[int, int]):
        super().__init__(x, y, direction)
        self.shape.color = pygame.color.THECOLORS['green']


class Laser(Projectile):
    """
    Bullet class.
    """

    def __init__(self, x: int, y: int, direction: tuple[int, int]):
        super().__init__(x, y, direction)
        self.shape.color = pygame.color.THECOLORS['red']
