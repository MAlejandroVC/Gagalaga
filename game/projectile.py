"""
This module contains the Projectile interface and its concrete implementations.
Concrete implementations are: Bullet, Rocket, and Laser.
"""

import pygame
import pymunk
from abc import ABC
from game.singleton import SpaceSingleton
from game import settings


class Projectile(ABC):
    """
    Projectile interface.
    """
    SHOOT_UP = (0, -1)
    SHOOT_DOWN = (0, 1)

    def __init__(self, x: int, y: int, direction: tuple[int, int], radius: float = 5, impulse: int = 1000):
        self.body = None
        self.shape = None
        self.space = SpaceSingleton()
        self.destroyed = False

        self.PROJECTILE_MASS = 1
        self.PROJECTILE_RADIUS = radius
        self.PROJECTILE_MOMENT = pymunk.moment_for_circle(self.PROJECTILE_MASS, 0, self.PROJECTILE_RADIUS)
        self.PROJECTILE_ELASTICITY = 0
        self.PROJECTILE_FRICTION = 1

        self.IMPULSE_CONSTANT = impulse
        self.CENTER_OF_GRAVITY = (0, 0)

        self.body = pymunk.Body(self.PROJECTILE_MASS, self.PROJECTILE_MOMENT)
        self.body.position = x, y
        self.shape = pymunk.Circle(self.body, self.PROJECTILE_RADIUS)
        self.shape.elasticity = self.PROJECTILE_ELASTICITY
        self.shape.friction = self.PROJECTILE_FRICTION
        self.body.apply_impulse_at_local_point((direction[0], direction[1]*impulse), self.CENTER_OF_GRAVITY)
        self.shape.color = pygame.color.THECOLORS['white']
        self.shape.collision_type = settings.PROJECTILE_COLLISION_TYPE
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
    # Projectile Image
    BULLET_IMAGE = pygame.image.load('assets/Weapons/Bullet.png')

    def __init__(self, x: int, y: int, direction: tuple[int, int]):
        super().__init__(x, y, direction, radius=5, impulse=1000)
        self.shape.color = pygame.color.THECOLORS['blue']

    def draw(self, screen: pygame.Surface) -> None:
        """
        Draws the projectile.
        :param screen: screen to draw on.
        :return: None
        """
        x, y = self.body.position
        scaled_image = pygame.transform.scale(self.BULLET_IMAGE, (self.PROJECTILE_RADIUS*4, self.PROJECTILE_RADIUS*4))
        screen.blit(scaled_image, (x - self.PROJECTILE_RADIUS*2, y - self.PROJECTILE_RADIUS*2))


class Rocket(Projectile):
    """
    Bullet class.
    """
    # Projectile Image
    ROCKET_IMAGE = pygame.image.load('assets/Weapons/Rocket.png')

    def __init__(self, x: int, y: int, direction: tuple[int, int]):
        super().__init__(x, y, direction, radius=25, impulse=500)
        self.shape.color = pygame.color.THECOLORS['green']

    def draw(self, screen: pygame.Surface) -> None:
        """
        Draws the projectile.
        :param screen: screen to draw on.
        :return: None
        """
        x, y = self.body.position
        scaled_image = pygame.transform.scale(self.ROCKET_IMAGE,
                                              (self.PROJECTILE_RADIUS * 4, self.PROJECTILE_RADIUS * 4))
        screen.blit(scaled_image, (x - self.PROJECTILE_RADIUS * 2, y - self.PROJECTILE_RADIUS * 2))


class Laser(Projectile):
    """
    Bullet class.
    """
    # Projectile Image
    LASER_IMAGE = pygame.image.load('assets/Weapons/Laser.png')

    def __init__(self, x: int, y: int, direction: tuple[int, int]):
        super().__init__(x, y, direction, radius=10, impulse=2000)
        self.shape.color = pygame.color.THECOLORS['red']

    def draw(self, screen: pygame.Surface) -> None:
        """
        Draws the projectile.
        :param screen: screen to draw on.
        :return: None
        """
        x, y = self.body.position
        scaled_image = pygame.transform.scale(self.LASER_IMAGE,
                                              (self.PROJECTILE_RADIUS * 4, self.PROJECTILE_RADIUS * 4))
        screen.blit(scaled_image, (x - self.PROJECTILE_RADIUS * 2, y - self.PROJECTILE_RADIUS * 2))
