"""
Galaga game
"""

import pygame
import pymunk
import pymunk.pygame_util
from game import settings
from game.player import Player
from game.enemy import Enemy
from game.singleton import *

# Initialize pygame
pygame.init()
screen_singleton = ScreenSingleton(settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT)
clock = pygame.time.Clock()
space = SpaceSingleton()

# Create a player
player = Player(Player.STARTING_X, Player.STARTING_Y)

# Create enemies
enemy_timer = 0
enemies = []
# for i in range(settings.TOTAL_RANKS):
#     for j in range(settings.TOTAL_FILES - 3):
#         enemies.append(Enemy(settings.SCREEN_RANK[i], settings.SCREEN_FILE[j]))

# Draw options
draw_options = pymunk.pygame_util.DrawOptions(screen_singleton.screen)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear screen
    screen_singleton.screen.fill(settings.SCREEN_COLOR)

    enemy_timer += clock.get_time()
    if enemy_timer >= settings.ENEMY_CREATION_INTERVAL and len(enemies) < 10:
        enemies.append(Enemy(settings.SCREEN_RANK[0], settings.SCREEN_FILE[0]))
        enemy_timer = 0

    # Draw stuff
    space.debug_draw(draw_options)
    player.draw()
    for enemy in enemies:
        enemy.draw()

    # Update physics
    dt = 1.0 / settings.UPDATES_PER_SECOND
    for x in range(1):
        space.step(dt)

    # Move player
    keys = pygame.key.get_pressed()
    player.player_key(keys)

    # Move enemies
    for enemy in enemies:
        enemy.move()

    # Clock
    pygame.display.flip()
    clock.tick(settings.FRAMES_PER_SECOND)

pygame.quit()
