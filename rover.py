from position import CardinalPoint, Position


class Rover:
    def __init__(self, position: Position, faced_direction: CardinalPoint):
        self.position = position
        self.faced_direction = faced_direction
        self.last_avoided_obstacle = None

    def move_forward(self):
        self._move_towards_faced_direction()

    def move_backward(self):
        self.faced_direction = self.faced_direction.opposite
        self.move_forward()

    def turn_left(self):
        self.faced_direction = self.faced_direction.left

    def turn_right(self):
        self.faced_direction = self.faced_direction.right

    def _move_towards_faced_direction(self):
        potential_new_positions = {
            CardinalPoint.N: self.position.increment_y(),
            CardinalPoint.S: self.position.decrement_y(),
            CardinalPoint.E: self.position.increment_x(),
            CardinalPoint.W: self.position.decrement_x(),
        }

        cardinal_point_faced = self.faced_direction
        potential_new_position = potential_new_positions[cardinal_point_faced]

        if potential_new_position.has_no_obstacle():
            self.position = potential_new_position
        else:
            self.last_avoided_obstacle = potential_new_position
