"""This module implements utilities to help handle the location functions of the Mars Rover"""

from enum import Enum


class Position:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def increment_y(self):
        self.y += 1

    def decrement_y(self):
        self.y -= 1

    def increment_x(self):
        self.x += 1

    def decrement_x(self):
        self.x -= 1


class CardinalPoint(Enum):
    N = "N"
    S = "S"
    E = "E"
    W = "W"
