"""
Galaga game
"""

import pygame
import pymunk
import pymunk.pygame_util

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((1250, 750))
clock = pygame.time.Clock()
running = True

# Initialize pymunk
space = pymunk.Space()
space.gravity = 0, 0

# Create a player
player = Player()
space.add(player.body, player.shape)

# Draw options
draw_options = pymunk.pygame_util.DrawOptions(screen)

# Game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear screen
    screen.fill((0, 0, 0))

    # Draw stuff
    space.debug_draw(draw_options)

    # Update physics
    dt = 1.0 / 60.0
    for x in range(1):
        space.step(dt)

    # Move player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w or pygame.K_a or pygame.K_s or pygame.K_d or pygame.K_SPACE]:
        # player.move()
        pass

    # Clock
    clock.tick(50)

pygame.quit()
