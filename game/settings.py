"""
This module handles the settings of the game.
"""

# Settings Magic Numbers
SCREEN_WIDTH = 1250
SCREEN_HEIGHT = 750
SCREEN_COLOR = (0, 0, 0)

SHIP_WIDTH = 50
SHIP_HEIGHT = 50

GRAVITY_X = 0
GRAVITY_Y = 0

UPDATES_PER_SECOND = 60.0
FRAMES_PER_SECOND = 60

PADDING = 25

# Files (y)
TOTAL_FILES = SCREEN_HEIGHT // (SHIP_HEIGHT + PADDING)
SCREEN_FILE_DIFF = SHIP_HEIGHT + PADDING
SCREEN_FILE = [PADDING*2]
for i in range(1, TOTAL_FILES):
    SCREEN_FILE.append(SCREEN_FILE[i - 1] + SCREEN_FILE_DIFF)

# Ranks (x)
TOTAL_RANKS = SCREEN_WIDTH // (SHIP_WIDTH + PADDING)
SCREEN_RANK_DIFF = SHIP_WIDTH + PADDING
SCREEN_RANK = [PADDING]
for i in range(1, TOTAL_RANKS):
    SCREEN_RANK.append(SCREEN_RANK[i - 1] + SCREEN_RANK_DIFF)


def is_even_file(y_position) -> bool:
    """
    Returns True if the y_position is in an even y.
    Allows for a 5 pixel error.
    """
    for file in SCREEN_FILE[::2]:
        if abs(y_position - file) <= 5:
            return True
    return False


def is_odd_file(y_position) -> bool:
    """
    Returns True if the y_position is in an odd y.
    Allows for a 5 pixel error.
    """
    for file in SCREEN_FILE[1::2]:
        if abs(y_position - file) <= 5:
            return True
    return False


# Game Difficulty
EASY = 1
MEDIUM = 2
HARD = 3

# Collision Types
DEFAULT_COLLISION_TYPE = 0
PLAYER_COLLISION_TYPE = 1
PROJECTILE_COLLISION_TYPE = 2
ENEMY_COLLISION_TYPE = 3
