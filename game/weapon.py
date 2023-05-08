"""
This module contains the Weapon class and its decorators.
Concrete decorators are: Gun, RocketLauncher, and LaserCannon.
"""
from game.projectile import *
import time


class Weapon:
    """
    Weapon decorator class.
    """
    # Weapon Magic Numbers
    BURST = 1
    BURST_COOLDOWN = .1

    def __init__(self, ship):
        self.ship = ship
        self.projectiles = []

        self.burst_count = 0
        self.time_since_last_shot = 0

    def shoot(self, direction: tuple[int, int]) -> None:
        """
        Shoots a projectile in a given direction if the burst count is less than the burst limit.
        The burst count is reset if the burst cooldown has passed.
        :param direction: direction to shoot in.
        :return: None
        """
        if self.burst_count < self.BURST:
            self.launch_projectile(direction)
            self.burst_count += 1
            self.time_since_last_shot = time.time()
        else:
            if time.time() - self.time_since_last_shot >= self.BURST_COOLDOWN:
                self.time_since_last_shot = 0
                self.burst_count = 0

    def launch_projectile(self, direction: tuple[int, int]) -> None:
        """
        Launches a projectile in a given direction.
        :param direction: direction to launch in.
        :return: None
        """
        adjusted_position = self.ship.body.position.x + self.ship.vertices[1][0], \
                            self.ship.body.position.y + self.ship.vertices[1][1]
        self.projectiles.append(self.get_projectile_instance(adjusted_position[0], adjusted_position[1], direction))

    def get_projectile_instance(self, x: int, y: int, direction: tuple[int, int]) -> None:
        """
        Returns a projectile instance.
        This method is overridden by the concrete decorators.
        :param x: x coordinate.
        :param y: y coordinate.
        :param direction: direction to launch in.
        :return: None
        """
        pass


class Gun(Weapon):
    """
    Gun concrete decorator.
    """
    # Gun Magic Numbers
    BURST = 3
    BURST_COOLDOWN = 0.5

    def get_projectile_instance(self, x: int, y: int, direction: tuple[int, int]) -> Bullet:
        """
        Returns a bullet instance.
        :param x: x coordinate.
        :param y: y coordinate.
        :param direction: direction to launch in.
        :return: Bullet instance.
        """
        return Bullet(x, y, direction)


class RocketLauncher(Weapon):
    """
    Rocket Launcher concrete decorator.
    """
    # Rocket Launcher Magic Numbers
    BURST = 2
    BURST_COOLDOWN = 1

    def get_projectile_instance(self, x: int, y: int, direction: tuple[int, int]) -> Rocket:
        """
        Returns a rocket instance.
        :param x: x coordinate.
        :param y: y coordinate.
        :param direction: direction to launch in.
        :return: Rocket instance.
        """
        return Rocket(x, y, direction)


class LaserCannon(Weapon):
    """
    Laser Cannon concrete decorator.
    """
    # Laser Cannon Magic Numbers
    BURST = 10
    BURST_COOLDOWN = 1

    def get_projectile_instance(self, x: int, y: int, direction: tuple[int, int]) -> Laser:
        """
        Returns a laser instance.
        :param x: x coordinate.
        :param y: y coordinate.
        :param direction: direction to launch in.
        :return: Laser instance.
        """
        return Laser(x, y, direction)
