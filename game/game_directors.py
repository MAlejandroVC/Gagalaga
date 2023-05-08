import pygame
from game import settings
from game.player import Player
from game.enemy import Enemy
from game.weapon import *
from game.projectile import Projectile


class GameObjectFactory:
    def __init__(self, space):
        self.space = space

    def create_player(self, x, y):
        player = Player(x, y)
        # Add player body to physics space
        self.space.add(player.body, player.shape)
        # Add Gun decorator to player
        player.add_weapon(LaserCannon)

        return player

    def create_enemy(self, rank, file):
        enemy = Enemy(rank, file)
        # Add enemy body to physics space
        self.space.add(enemy.body, enemy.shape)

        return enemy

    def create_projectile(self, x, y, direction):
        projectile = Projectile(x, y, direction)
        # Add projectile body to physics space
        self.space.add(projectile.body, projectile.shape)

        return projectile


def on_collision(arbiter, space, data):
    # Get colliding objects
    shape_1, shape_2 = arbiter.shapes

    # Remove colliding objects from physics space
    space.remove(shape_1, shape_2)

    # Destroy colliding objects
    shape_1.belonging_object.destroy()
    shape_2.belonging_object.destroy()

    return True


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

        # Remove destroyed objects from game
        if self.player.destroyed:
            # TODO: Game over
            return
        self.enemies = [enemy for enemy in self.enemies if not enemy.destroyed]
        for weapon in self.player.weapons:
            weapon.projectiles = [projectile for projectile in weapon.projectiles if not projectile.destroyed]

        # Update physics simulation
        dt = 1.0 / settings.UPDATES_PER_SECOND
        for x in range(1):
            self.space.step(dt)


class GameRenderer:
    def __init__(self, screen, space, draw_options):
        self.screen = screen
        self.space = space
        self.draw_options = draw_options

    def render(self, player, enemies):
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
