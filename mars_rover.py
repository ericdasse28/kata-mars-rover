from dataclasses import dataclass
from enum import Enum


@dataclass
class Point:
    x: float
    y: float


class CardinalPoint(Enum):
    N = "N"
    S = "S"
    E = "E"
    W = "W"


class Rover:
    def __init__(self, position, direction):
        self.position = position
        self.direction = direction

    def move_forward(self):
        if self.direction == CardinalPoint.S:
            self.position.y -= 1
        elif self.direction == CardinalPoint.N:
            self.position.y += 1
        elif self.direction == CardinalPoint.E:
            self.position.x += 1
        elif self.direction == CardinalPoint.W:
            self.position.x -= 1

    def move_backward(self):
        if self.direction == CardinalPoint.N:
            self.position.y -= 1
            self.direction = CardinalPoint.S
        elif self.direction == CardinalPoint.S:
            self.position.y += 1
            self.direction = CardinalPoint.N
