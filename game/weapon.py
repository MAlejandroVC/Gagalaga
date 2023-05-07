"""
Weapon module.
Weapon class and its decorators.
"""

from game.projectile import *


class Weapon:
    """
    Weapon decorator class.
    """
    def __init__(self, ship):
        self.ship = ship

    def shoot(self, direction):
        pass


class Gun(Weapon):
    """
    Gun decorator class.
    """
    def __init__(self, ship):
        super().__init__(ship)

    def shoot(self, direction):
        adjusted_position = self.ship.body.position.x + self.ship.vertices[1][0], \
                            self.ship.body.position.y + self.ship.vertices[1][1]
        self.ship.projectiles.append(Bullet(adjusted_position[0], adjusted_position[1], direction))
