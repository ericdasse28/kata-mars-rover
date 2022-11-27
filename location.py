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

    @property
    def left(self):
        """Assuming we are facing the instance cardinal point,
        returns the cardinal point on the its left
        """

        left_dictionary = {
            CardinalPoint.S: CardinalPoint.E,
            CardinalPoint.N: CardinalPoint.W,
        }

        left_cardinal_point = left_dictionary[self]
        return left_cardinal_point

    @property
    def opposite(self):
        """Assuming we are facing the instance cardinal point,
        returns the opposite cardinal point
        """

        opposite_dictionary = {
            CardinalPoint.N: CardinalPoint.S,
            CardinalPoint.S: CardinalPoint.N,
            CardinalPoint.E: CardinalPoint.W,
            CardinalPoint.W: CardinalPoint.E,
        }

        opposite_cardinal_point = opposite_dictionary[self]
        return opposite_cardinal_point
