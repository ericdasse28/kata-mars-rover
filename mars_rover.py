from dataclasses import dataclass
from enum import Enum


@dataclass
class Point:
    x: float
    y: float


class CardinalPoint(Enum):
    N = "N"
    S = "S"


class Rover:
    def __init__(self, position, direction):
        self.position = position
        self.direction = direction

    def move_forward(self):
        if self.direction == CardinalPoint.S:
            self.position.y -= 1
        else:
            self.position.y += 1
