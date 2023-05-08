"""
This module handles the main class of the game:
GameObjectFactory, GameLogic, GameRenderer, and Engine.
"""
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
        player.equip_weapon(Gun)

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

    def create_enemy_army(self, files: int) -> list[Enemy]:
        """
        Creates an enemy army.
        :param files: number of files in the army.
        :return: list of enemies.
        """
        enemies = []
        for file in settings.SCREEN_FILE[:files]:
            if settings.is_even_file(file):
                start = 0
            else:
                start = 1
            for rank in settings.SCREEN_RANK[start::2]:
                enemies.append(self.create_enemy(rank, file))

        return enemies


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
        # Check for game over
        if self.is_game_over():
            return True

        # Update positions
        self.__update_positions(keys)

        # Destroy objects that are out of bounds
        self.__destroy_out_of_bounds_objects()

        # Remove destroyed objects from game
        self.__remove_destroyed_objects()

        # Update physics simulation
        self.__update_physics()

        return False

    def is_game_over(self) -> bool:
        """
        Checks if game is over.
        :return: True if game over, False otherwise.
        """
        if self.player.destroyed:
            return True
        if not self.enemies:
            return True
        return False

    def __update_positions(self, keys: pygame.key.ScancodeWrapper) -> None:
        """
        Updates game object positions.
        :return: None.
        """
        # Update player position based on user input
        self.player.player_key(keys)

        # Update enemy positions
        for enemy in self.enemies:
            enemy.move()

    def __destroy_out_of_bounds_objects(self) -> None:
        """
        Destroys objects that are out of bounds.
        :return: None.
        """
        # Destroy projectiles that are out of bounds
        for projectile in self.player.weapon.projectiles:
            if projectile.body.position.y < 0:
                projectile.destroy()
        # Destroy enemies that are out of bounds
        for enemy in self.enemies:
            if enemy.body.position.x > settings.SCREEN_WIDTH + settings.SHIP_WIDTH \
                    or enemy.body.position.x < 0:
                enemy.destroy()
        # Destroy player if out of bounds
        if self.player.body.position.x > settings.SCREEN_WIDTH + settings.SHIP_WIDTH \
                or self.player.body.position.x < 0:
            self.player.destroy()

    def __remove_destroyed_objects(self) -> None:
        self.enemies = [enemy for enemy in self.enemies if not enemy.destroyed]
        self.player.weapon.projectiles = [projectile for projectile in self.player.weapon.projectiles if
                                          not projectile.destroyed]

    def __update_physics(self) -> None:
        """
        Updates physics simulation.
        :return: None.
        """
        dt = 1.0 / settings.UPDATES_PER_SECOND
        for x in range(1):
            self.space.step(dt)


class GameRenderer:
    """
    Game renderer class for rendering game objects.
    """
    def __init__(self, screen: pygame.Surface, space: pymunk.Space, draw_options: pymunk.pygame_util.DrawOptions, debug: bool = False):
        self.screen = screen
        self.space = space
        self.draw_options = draw_options
        self.debug = debug

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
        if player.weapon:
            for projectile in player.weapon.projectiles:
                projectile.draw(self.screen)
        for enemy in enemies:
            enemy.draw(self.screen)
            if enemy.weapon:
                for projectile in enemy.weapon.projectiles:
                    projectile.draw(self.screen)

        # Draw physics debug information
        if self.debug:
            self.space.debug_draw(self.draw_options)

        # Update display
        pygame.display.flip()

    def render_game_over(self) -> None:
        """
        Renders game over screen.
        :return: None.
        """
        # Clear screen
        self.screen.fill(settings.SCREEN_COLOR)

        # Draw game over image
        image = pygame.image.load('assets/Other/game_over.png')
        self.screen.blit(image, (settings.SCREEN_WIDTH / 2 - image.get_width() / 2, settings.SCREEN_HEIGHT / 2 - image.get_height() / 2))

        # Update display
        pygame.display.flip()


class Engine:
    """
    Engine class for housing static methods.
    """

    @staticmethod
    def on_collision_player(arbiter, space: pymunk.Space, data) -> bool:
        """
        Collision handler.
        :param arbiter: ???
        :param space: space object.
        :param data: ???
        :return: True if collision handled, False otherwise.
        """
        # Get colliding objects
        shape_1, shape_2 = arbiter.shapes

        # Destroy colliding objects
        shape_1.belonging_object.destroy()
        shape_2.belonging_object.destroy()

        return True

    @staticmethod
    def on_collision_enemy(arbiter, space: pymunk.Space, data) -> bool:
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
