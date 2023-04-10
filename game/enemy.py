"""
This module contains the Enemy class.

"""
import pygame
from game.ship import Ship
from game import settings


class Enemy(Ship):
    """
    Enemy class.
    Extends the Ship class.
    """

    def __int__(self, starting_x, starting_y):
        super().__init__(starting_x, starting_y)
