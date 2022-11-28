"""This module implements utilities to help handle the location functions of the Mars Rover"""
import mars

from enum import Enum


class Planet:
    """Represents the planet on which the rover is moving.
    Default to Mars."""

    def __init__(self, name="Mars", radius=None):
        self.name = name
        if radius is None:
            radius = mars.RADIUS
        self.radius = radius
        self.obstacles_coordinates = []

    def compute_y_increment(self, y_value):
        if y_value == self.radius:
            return -y_value
        return y_value + 1

    def compute_y_decrement(self, y_value):
        if y_value == -self.radius:
            return -y_value
        return y_value - 1

    def compute_x_increment(self, x_value):
        if x_value == self.radius:
            return -x_value
        return x_value + 1

    def compute_x_decrement(self, x_value):
        if x_value == -self.radius:
            return -x_value
        return x_value - 1

    def add_obstacle(self, x, y):
        self.obstacles_coordinates.append((x, y))


class Position:
    def __init__(self, x: float, y: float, planet: Planet = None):
        self.x = x
        self.y = y
        if planet is None:
            planet = Planet()
        self.planet = planet

    def increment_y(self):
        self.y = self.planet.compute_y_increment(self.y)

    def decrement_y(self):
        self.y = self.planet.compute_y_decrement(self.y)

    def increment_x(self):
        self.x = self.planet.compute_x_increment(self.x)

    def decrement_x(self):
        self.x = self.planet.compute_x_decrement(self.x)


class CardinalPoint(Enum):
    N = "N"
    S = "S"
    E = "E"
    W = "W"

    @property
    def right(self):
        """Assuming we are facing the instance cardinal point,
        returns the cardinal point on its right"""

        right_dictionary = {
            CardinalPoint.S: CardinalPoint.W,
            CardinalPoint.N: CardinalPoint.E,
            CardinalPoint.E: CardinalPoint.S,
            CardinalPoint.W: CardinalPoint.N,
        }

        right_cardinal_point = right_dictionary[self]
        return right_cardinal_point

    @property
    def left(self):
        """Assuming we are facing the instance cardinal point,
        returns the cardinal point on the its left
        """

        left_dictionary = {
            CardinalPoint.S: CardinalPoint.E,
            CardinalPoint.N: CardinalPoint.W,
            CardinalPoint.E: CardinalPoint.N,
            CardinalPoint.W: CardinalPoint.S,
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
