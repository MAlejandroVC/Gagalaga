import pygame
import pymunk
import pymunk.pygame_util
from game import settings
from game.player import Player
from game.enemy import Enemy
from game.singleton import *


class GameObjectFactory:
    def __init__(self, space):
        self.space = space

    def create_player(self, x, y):
        player = Player(x, y)
        # Add player body to physics space
        self.space.add(player.body, player.shape)
        return player

    def create_enemy(self, rank, file):
        enemy = Enemy(rank, file)
        # Add enemy body to physics space
        self.space.add(enemy.body, enemy.shape)
        return enemy


class GameLogic:
    def __init__(self, space, player, enemies):
        self.space = space
        self.player = player
        self.enemies = enemies

    def update(self, keys):
        # Update player position based on user input
        self.player.player_key(keys)

        # Update enemy positions
        for enemy in self.enemies:
            enemy.move()

        # Check for collisions between player and enemies
        for enemy in self.enemies:
            if self.player.collides_with(enemy):
                self.player.hit()

        # Check for collisions between enemies and projectiles
        for projectile in self.player.projectiles:
            for enemy in self.enemies:
                if enemy.collides_with(projectile):
                    enemy.hit()
                    # Remove projectile from space
                    self.space.remove(projectile.body, projectile.shape)
                    self.player.projectiles.remove(projectile)
                    break

        # Destroy ships that have been hit
        # if self.player.destroyed:
        #     self.space.remove(self.player.body, self.player.shape)
        #     self.player.destroy()
        #
        # for enemy in self.enemies:
        #     if enemy.destroyed:
        #         self.space.remove(enemy.body, enemy.shape)
        #         self.enemies.remove(enemy)

        # Update physics simulation
        dt = 1.0 / settings.UPDATES_PER_SECOND
        for x in range(1):
            self.space.step(dt)


class GameRenderer:
    def __init__(self, screen, space, draw_options):
        self.screen = screen
        self.space = space
        self.draw_options = draw_options

    def render(self, player, enemies, projectiles):
        # Clear screen
        self.screen.fill(settings.SCREEN_COLOR)

        # Draw objects
        player.draw(self.screen)
        for enemy in enemies:
            enemy.draw(self.screen)
        for projectile in projectiles:
            projectile.draw(self.screen)

        # Draw physics debug information
        self.space.debug_draw(self.draw_options)

        # Update display
        pygame.display.flip()

