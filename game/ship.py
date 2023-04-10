"""
This module contains the Space-ship class.
The ship class handles the physics of the ship.
The ship class is shared by the player and the enemy.
"""
import pygame
import pymunk
import pymunk.pygame_util

from game import settings
from game.weapon import Projectile
from game.singleton import *


class Ship:
    """
    Space-ship class.
    """

    # Physics Magic Numbers
    SHIP_MASS = 1
    SHIP_MOMENT = 10000000
    SHIP_CENTER_OF_GRAVITY = (0, 0)

    # Thrust Magic Numbers
    THRUST_CONSTANT = 250
    THRUST_UP = (0, -1*THRUST_CONSTANT)  # Thrust vector pointing upwards
    THRUST_DOWN = (0, 1*THRUST_CONSTANT)  # Thrust vector pointing downwards
    THRUST_LEFT = (-1*THRUST_CONSTANT, 0)  # Thrust vector pointing left
    THRUST_RIGHT = (1*THRUST_CONSTANT, 0)  # Thrust vector pointing right
    THRUST_NONE = (0, 0)  # No thrust

    __space = SpaceSingleton()

    def __init__(self, x, y):
        self.body = pymunk.Body(self.SHIP_MASS, self.SHIP_MOMENT)
        self.body.position = x, y
        shape = TriangleShape(self.body, self.VERTICES, self.COLOR)

        self.__space.add(self.body, shape)

    def move(self, thrust_direction):
        """
        Applies a force to the ship in the given direction.
        :param thrust_direction: direction in which the force is applied using Ship.THRUST_DIRECTION.
        """
        # self.body.apply_force_at_local_point(thrust_direction, self.SHIP_CENTER_OF_GRAVITY)
        self.body.velocity = thrust_direction

    def shoot(self, direction):
        """
        Makes the ship shoot a projectile.
        """
        adjusted_position = self.body.position.x + self.VERTICES[1][0], self.body.position.y + self.VERTICES[1][1]
        projectile = Projectile(adjusted_position[0], adjusted_position[1], direction)

        self.__space.add(projectile.body, projectile.shape)


class TriangleShape(pymunk.Poly):
    """
    Triangle shape class.
    """

    # Shape Magic Numbers
    TRIANGLE_ELASTICITY = 0
    TRIANGLE_FRICTION = 1

    def __init__(self, body, vertices, color=(255, 0, 255, 0)):
        super().__init__(body, vertices)
        self.elasticity = self.TRIANGLE_ELASTICITY
        self.friction = self.TRIANGLE_FRICTION
        self.color = color
