"""

"""

import pygame
import pymunk
import pymunk.pygame_util
from abc import ABC, abstractmethod


class Weapon(ABC):
    # TODO: add weapon class
    pass


class Projectile:
    """
    Projectile class.
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
        self.body = pymunk.Body(self.PROJECTILE_MASS, self.PROJECTILE_MOMENT)
        self.body.position = x, y
        self.shape = pymunk.Circle(self. body, self.PROJECTILE_RADIUS)
        self.shape.elasticity = self.PROJECTILE_ELASTICITY
        self.shape.friction = self.PROJECTILE_FRICTION
        if direction == 'up':
            self.body.apply_impulse_at_local_point(self.IMPULSE_UP, self.CENTER_OF_GRAVITY)
        elif direction == 'down':
            self.body.apply_impulse_at_local_point(self.IMPULSE_DOWN, self.CENTER_OF_GRAVITY)
        self.shape.color = pygame.color.THECOLORS['red']
