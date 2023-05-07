"""
This module contains the Space-ship class.
The ship class handles the physics of the ship.
The ship class is shared by the player and the enemy.
"""
import pygame
import pymunk
import pymunk.pygame_util
from game import settings


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

    def __init__(self, x, y, vertices, color=(255, 0, 255, 0)):
        self.body = pymunk.Body(self.SHIP_MASS, self.SHIP_MOMENT)
        self.body.position = x, y
        self.vertices = vertices
        self.shape = TriangleShape(self.body, vertices, color)
        self.shape.color = color
        self.destroyed = False
        self.weapons = []
        self.projectiles = []

    def move(self, thrust_direction):
        """
        Applies a force to the ship in the given direction.
        :param thrust_direction: direction in which the force is applied using Ship.THRUST_DIRECTION.
        """
        # self.body.apply_force_at_local_point(thrust_direction, self.SHIP_CENTER_OF_GRAVITY)
        self.body.velocity = thrust_direction

    def draw(self, screen, image, x, y):
        """
        Draws the ship on the screen.
        """
        scaled_image = pygame.transform.scale(image, (settings.SHIP_WIDTH*2, settings.SHIP_HEIGHT*2))

        screen.blit(scaled_image, (x, y))

    def add_weapon(self, weapon):
        """
        Adds a weapon to the ship.
        :param weapon: weapon to add.
        """
        self.weapons.append(weapon(self))

    def shoot(self, direction):
        """
        Makes the ship shoot a projectile.
        """
        for weapon in self.weapons:
            weapon.shoot(direction)

    def collides_with(self, other):
        """
        Checks if the ship collides with another object.
        :param other: object to check collision with.
        :return: True if the ship collides with the object, False otherwise.
        """
        return self.shape.shapes_collide(other.shape)

    def hit(self):
        """
        Handles the ship being hit.
        When the ship is hit, the ship is destroyed.
        """
        # TODO: Explosion animation
        self.destroyed = True
        self.shape.color = (255, 0, 0, 0)


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
