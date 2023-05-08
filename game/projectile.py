"""
Projectile module
Projectile interface and its implementations.
"""

import pygame
import pymunk
from abc import ABC, abstractmethod

from game import settings
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
    IMPULSE_UP = (0, -1 * IMPULSE_CONSTANT)
    IMPULSE_DOWN = (0, 1 * IMPULSE_CONSTANT)
    CENTER_OF_GRAVITY = (0, 0)

    def __init__(self, x, y, direction):
        self.body = None
        self.shape = None
        self.space = SpaceSingleton()
        self.destroyed = False

        self.body = pymunk.Body(self.PROJECTILE_MASS, self.PROJECTILE_MOMENT)
        self.body.position = x, y
        self.shape = pymunk.Circle(self.body, self.PROJECTILE_RADIUS)
        self.shape.elasticity = self.PROJECTILE_ELASTICITY
        self.shape.friction = self.PROJECTILE_FRICTION
        if direction == 'up':
            self.body.apply_impulse_at_local_point(self.IMPULSE_UP, self.CENTER_OF_GRAVITY)
        elif direction == 'down':
            self.body.apply_impulse_at_local_point(self.IMPULSE_DOWN, self.CENTER_OF_GRAVITY)
        self.shape.color = pygame.color.THECOLORS['white']
        self.space.add(self.body, self.shape)
        self.shape.belonging_object = self

    def draw(self, screen):
        """
        Draws the projectile.
        """
        position = int(self.body.position.x), int(self.body.position.y)
        pygame.draw.circle(screen, self.shape.color, position, self.shape.radius)

    def destroy(self):
        """
        Destroys the projectile.
        """
        self.destroyed = True


class Bullet(Projectile):
    """
    Bullet class.
    """
    IMPULSE_CONSTANT = 1000

    def __init__(self, x, y, direction):
        super().__init__(x, y, direction)
        self.shape.color = pygame.color.THECOLORS['blue']


class Rocket(Projectile):
    """
    Bullet class.
    """
    IMPULSE_CONSTANT = 750

    def __init__(self, x, y, direction):
        super().__init__(x, y, direction)
        self.shape.color = pygame.color.THECOLORS['green']


class Laser(Projectile):
    """
    Bullet class.
    """
    IMPULSE_CONSTANT = 1250

    def __init__(self, x, y, direction):
        super().__init__(x, y, direction)
        self.shape.color = pygame.color.THECOLORS['red']
