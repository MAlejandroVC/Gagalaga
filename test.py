"""
Using Pymunk make a black space witch a square that can be moved with WASD
"""

import pygame
import pymunk
import pymunk.pygame_util


def shoot(space, position, impulse):
    mass = 1
    radius = 5
    moment = pymunk.moment_for_circle(mass, 0, radius)
    body = pymunk.Body(mass=mass, moment=moment)
    body.position = position
    shape = pymunk.Circle(body, radius)
    space.add(body, shape)
    point = (0, 0) # Point at the center of gravity of the body
    body.apply_impulse_at_local_point(impulse, point)


# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((1250, 750))
clock = pygame.time.Clock()
running = True

# Initialize pymunk
space = pymunk.Space()
space.gravity = 0, 100

# Create a dynamic body and a box shape
body = pymunk.Body(1, 1000)
body.position = 300, 300
box = pymunk.Poly.create_box(body, (50, 50))
box.elasticity = 0.95
box.friction = 0.9
space.add(body, box)

# Create a floor
floor = pymunk.Body(body_type=pymunk.Body.STATIC)
floor.position = (0, 500)
floor_shape = pymunk.Segment(floor, (0, 0), (600, 0), 5)
floor_shape.elasticity = 0.15
floor_shape.friction = 1.0
space.add(floor, floor_shape)

# Create a thrust
thrust_up = (0, -500)  # Thrust vector pointing upwards
thrust_down = (0, 500)  # Thrust vector pointing downwards
thrust_left = (-500, 0)  # Thrust vector pointing left
thrust_right = (500, 0)  # Thrust vector pointing right
point = (0, 0)  # Point at the center of gravity of the body

# Draw options
draw_options = pymunk.pygame_util.DrawOptions(screen)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

    # Clear screen
    screen.fill((255, 255, 255))

    # Draw stuff
    space.debug_draw(draw_options)

    # Update physics
    dt = 1.0 / 60.0
    for x in range(1):
        space.step(dt)

    # Flip screen
    pygame.display.flip()
    clock.tick(50)

    # Move the box with WASD and shoot with space
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        body.apply_force_at_local_point(thrust_up, point)
    if keys[pygame.K_s]:
        body.apply_force_at_local_point(thrust_down, point)
    if keys[pygame.K_a]:
        body.apply_force_at_local_point(thrust_left, point)
    if keys[pygame.K_d]:
        body.apply_force_at_local_point(thrust_right, point)
    if keys[pygame.K_SPACE]:
        shoot(space, body.position, (0, -1000))

pygame.quit()
