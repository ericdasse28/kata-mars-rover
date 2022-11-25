from dataclasses import dataclass


@dataclass
class Point:
    x: float
    y: float


class Rover:
    def __init__(self, position, direction):
        self.position = position
        self.direction = direction

    def move_forward(self):
        if self.direction == "S":
            self.position.y = -1
        else:
            self.position.y += 1