"""
This module contains the Space-ship class.
The ship class handles the physics of the ship.
The ship class is shared by the player and the enemy.
"""
import pygame
import pymunk
import pymunk.pygame_util
from game import settings
from game.weapon import Weapon


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

    def __init__(self, x: int, y: int,
                 vertices: list[tuple[float, float]],
                 color: tuple[int, int, int, int] = (255, 0, 255, 0)):
        self.body = pymunk.Body(self.SHIP_MASS, self.SHIP_MOMENT)
        self.body.position = x, y
        self.vertices = vertices
        self.shape = TriangleShape(self.body, vertices, color)
        self.shape.color = color
        self.shape.belonging_object = self
        self.destroyed = False
        self.weapons = []

    def move(self, thrust_direction: tuple[int, int]) -> None:
        """
        Applies a force to the ship in the given direction.
        :param thrust_direction: direction in which the force is applied using Ship.THRUST_DIRECTION.
        :return: None
        """
        # self.body.apply_force_at_local_point(thrust_direction, self.SHIP_CENTER_OF_GRAVITY)
        self.body.velocity = thrust_direction

    def draw(self, screen: pygame.Surface, image: pygame.Surface, x: int, y: int) -> None:
        """
        Draws the ship on the screen.
        :param screen: screen to draw on.
        :param image: image to draw.
        :param x: x coordinate of the ship.
        :param y: y coordinate of the ship.
        :return: None
        """
        scaled_image = pygame.transform.scale(image, (settings.SHIP_WIDTH*2, settings.SHIP_HEIGHT*2))

        screen.blit(scaled_image, (x, y))

    def add_weapon(self, weapon) -> None:
        """
        Adds a weapon to the ship.
        :param weapon: weapon to add.
        :return: None
        """
        self.weapons.append(weapon(self))

    def shoot(self, direction: tuple[int, int]) -> None:
        """
        Makes the ship shoot a projectile.
        :param direction: direction in which the projectile is shot.
        :return: None
        """
        for weapon in self.weapons:
            weapon.shoot(direction)

    def destroy(self) -> None:
        """
        Destroys the ship.
        :return: None
        """
        self.body.position = -100, -100
        self.destroyed = True


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
