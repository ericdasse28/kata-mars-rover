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


def cardinal_opposite(cardinal_point: CardinalPoint):
    opposite_dictionary = {
        CardinalPoint.N: CardinalPoint.S,
        CardinalPoint.S: CardinalPoint.N,
        CardinalPoint.E: CardinalPoint.W,
        CardinalPoint.W: CardinalPoint.E,
    }

    opposite_cardinal_point = opposite_dictionary[cardinal_point]
    return opposite_cardinal_point
