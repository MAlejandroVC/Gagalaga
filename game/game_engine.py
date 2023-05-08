"""
This module handles the main class of the game:
GameObjectFactory, GameLogic, GameRenderer, and Engine.
"""
import pygame
import pymunk.pygame_util

from game import settings
from game.player import Player
from game.enemy import Enemy
from game.weapon import *


class GameObjectFactory:
    """
    Factory class for creating game objects.
    """
    def __init__(self, space: pymunk.Space):
        self.space = space

    def create_player(self, x: int, y: int) -> Player:
        """
        Creates a player object.
        :param x: x coordinate.
        :param y: y coordinate.
        :return: player object.
        """
        player = Player(x, y)
        # Add player body to physics space
        self.space.add(player.body, player.shape)
        # Add Gun decorator to player
        player.add_weapon(LaserCannon)

        return player

    def create_enemy(self, rank: int, file: int) -> Enemy:
        """
        Creates an enemy object.
        :param rank: x coordinate.
        :param file: y coordinate.
        :return: enemy object.
        """
        enemy = Enemy(rank, file)
        # Add enemy body to physics space
        self.space.add(enemy.body, enemy.shape)

        return enemy


class GameLogic:
    """
    Game logic class for updating game state.
    """
    def __init__(self, space: pymunk.Space, player: Player, enemies: list[Enemy]):
        self.space = space
        self.player = player
        self.enemies = enemies

    def update(self, keys: pygame.key.ScancodeWrapper) -> bool:
        """
        Updates game state.
        :param keys: user input.
        :return: True if game over, False otherwise.
        """
        # Update player position based on user input
        self.player.player_key(keys)

        # Update enemy positions
        for enemy in self.enemies:
            enemy.move()

        # Remove destroyed objects from game
        if self.player.destroyed:
            # TODO: Game over
            return True
        self.enemies = [enemy for enemy in self.enemies if not enemy.destroyed]
        for weapon in self.player.weapons:
            weapon.projectiles = [projectile for projectile in weapon.projectiles if not projectile.destroyed]

        # Update physics simulation
        dt = 1.0 / settings.UPDATES_PER_SECOND
        for x in range(1):
            self.space.step(dt)

        return False


class GameRenderer:
    """
    Game renderer class for rendering game objects.
    """
    def __init__(self, screen: pygame.Surface, space: pymunk.Space, draw_options: pymunk.pygame_util.DrawOptions):
        self.screen = screen
        self.space = space
        self.draw_options = draw_options

    def render(self, player: Player, enemies: list[Enemy]) -> None:
        """
        Renders game objects.
        :param player: player object.
        :param enemies: list of enemy objects.
        :return: None.
        """
        # Clear screen
        self.screen.fill(settings.SCREEN_COLOR)

        # Draw objects
        player.draw(self.screen)
        for projectile in [projectile for weapon in player.weapons for projectile in weapon.projectiles]:
            projectile.draw(self.screen)
        for enemy in enemies:
            enemy.draw(self.screen)
            for projectile in [projectile for weapon in enemy.weapons for projectile in weapon.projectiles]:
                projectile.draw(self.screen)

        # Draw physics debug information
        self.space.debug_draw(self.draw_options)

        # Update display
        pygame.display.flip()


class Engine:
    """
    Engine class for housing static methods.
    """

    @staticmethod
    def on_collision(arbiter, space: pymunk.Space, data) -> bool:
        """
        Collision handler.
        :param arbiter: ???
        :param space: space object.
        :param data: ???
        :return: True if collision handled, False otherwise.
        """
        # Get colliding objects
        shape_1, shape_2 = arbiter.shapes

        # Remove colliding objects from physics space
        space.remove(shape_1, shape_2)

        # Destroy colliding objects
        shape_1.belonging_object.destroy()
        shape_2.belonging_object.destroy()

        return True
