"""
Turn the Space class from Pymunk into a singleton.
"""

import pymunk
from game import settings


class SingletonMeta(type):
    """
    Singleton metaclass
    The SingletonMeta metaclass is used to create a singleton class
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class SpaceSingleton(pymunk.Space, metaclass=SingletonMeta):
    """
    Pymunk space singleton class
    """
    def __init__(self):
        super().__init__()
        self.gravity = settings.GRAVITY_X, settings.GRAVITY_Y
