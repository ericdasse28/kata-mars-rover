from location import CardinalPoint, Position


class Rover:
    def __init__(self, position: Position, faced_direction: CardinalPoint):
        self.position = position
        self.faced_direction = faced_direction

    def move_forward(self):
        self._move_towards(self.faced_direction)

    def move_backward(self):
        back_direction = self.faced_direction.opposite

        self.faced_direction = back_direction
        self._move_towards(self.faced_direction)

    def turn_left(self):
        self.faced_direction = self.faced_direction.left
        self._move_towards(self.faced_direction)

    def turn_right(self):
        self.faced_direction = self.faced_direction.right
        self._move_towards(self.faced_direction)

    def _move_towards(self, cardinal_point):
        movement_dictionary = {
            CardinalPoint.N: self.position.increment_y,
            CardinalPoint.S: self.position.decrement_y,
            CardinalPoint.E: self.position.increment_x,
            CardinalPoint.W: self.position.decrement_x,
        }

        movement = movement_dictionary[cardinal_point]
        movement()
