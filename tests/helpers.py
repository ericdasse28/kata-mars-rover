from location import CardinalPoint
from mars_rover import Rover


def assert_rover_state(
    rover: Rover, x: float, y: float, faced_direction: CardinalPoint
):
    assert rover.position.x == x
    assert rover.position.y == y
    assert rover.faced_direction == faced_direction
