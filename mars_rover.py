from location import CardinalPoint, Position


class Rover:
    def __init__(self, position: Position, faced_direction: CardinalPoint):
        self.position = position
        self.faced_direction = faced_direction

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
        elif self.direction == CardinalPoint.E:
            self.position.x -= 1
            self.direction = CardinalPoint.W
        elif self.direction == CardinalPoint.W:
            self.position.x += 1
            self.direction = CardinalPoint.E
