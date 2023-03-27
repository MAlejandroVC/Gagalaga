"""
This module contains the Space-ship class.
"""
import pygame
import pymunk
import pymunk.pygame_util
from game.weapon import Projectile
from game.singleton import *


class Ship:
    """
    Space-ship class.
    """

    # Ship Magic Numbers
    SHIP_MASS = 1
    SHIP_MOMENT = 1000
    SHIP_WIDTH = 50
    SHIP_HEIGHT = 50
    SHIP_ELASTICITY = 0
    SHIP_FRICTION = 1
    SHIP_CENTER_OF_GRAVITY = (0, 0)

    # Thrust Magic Numbers
    THRUST_CONSTANT = 500
    THRUST_UP = (0, -1*THRUST_CONSTANT)  # Thrust vector pointing upwards
    THRUST_DOWN = (0, 1*THRUST_CONSTANT)  # Thrust vector pointing downwards
    THRUST_LEFT = (-1*THRUST_CONSTANT, 0)  # Thrust vector pointing left
    THRUST_RIGHT = (1*THRUST_CONSTANT, 0)  # Thrust vector pointing right

    __space = SpaceSingleton()  # This feels wrong

    def __init__(self, x, y):
        self.body = pymunk.Body(self.SHIP_MASS, self.SHIP_MOMENT)
        self.body.position = x, y
        self.shape = pymunk.Poly.create_box(self.body, (self.SHIP_WIDTH, self.SHIP_HEIGHT))  # TODO: Change to a ship
        self.shape.elasticity = self.SHIP_ELASTICITY
        self.shape.friction = self.SHIP_FRICTION

        self.__space.add(self.body, self.shape)

    def move(self, direction):
        """
        Applies a force to the ship in the given direction.
        :param direction: direction in which the force is applied ('up', 'down', 'left', 'right').
        """
        if direction == 'up':
            self.body.apply_force_at_local_point(self.THRUST_UP, self.SHIP_CENTER_OF_GRAVITY)
        elif direction == 'down':
            self.body.apply_force_at_local_point(self.THRUST_DOWN, self.SHIP_CENTER_OF_GRAVITY)
        elif direction == 'left':
            self.body.apply_force_at_local_point(self.THRUST_LEFT, self.SHIP_CENTER_OF_GRAVITY)
        elif direction == 'right':
            self.body.apply_force_at_local_point(self.THRUST_RIGHT, self.SHIP_CENTER_OF_GRAVITY)

    def shoot(self):
        """
        Makes the ship shoot a projectile.
        """
        projectile = Projectile(self.body.position.x,
                                self.body.position.y - self.SHIP_HEIGHT/2 - Projectile.PROJECTILE_RADIUS,
                                'up')

        self.__space.add(projectile.body, projectile.shape)
