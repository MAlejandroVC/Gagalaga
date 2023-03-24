"""
Galaga game
"""

import pygame
import pymunk
import pymunk.pygame_util
from game import settings
from game.player import Player
from game.singleton import *

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
clock = pygame.time.Clock()

# Create Space Singleton
space = SpaceSingleton()

# Create a player
player = Player(Player.STARTING_X, Player.STARTING_Y)

# Create enemies
# TODO: create enemies

# Draw options
draw_options = pymunk.pygame_util.DrawOptions(screen)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear screen
    screen.fill(settings.SCREEN_COLOR)

    # Draw stuff
    space.debug_draw(draw_options)

    # Update physics
    dt = 1.0 / settings.UPDATES_PER_SECOND
    for x in range(1):
        space.step(dt)

    # Move player
    keys = pygame.key.get_pressed()
    player.move(keys)

    # Move enemies
    # TODO: move enemies

    # Clock
    pygame.display.flip()
    clock.tick(settings.FRAMES_PER_SECOND)

pygame.quit()
