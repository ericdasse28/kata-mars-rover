from position import CardinalPoint
from rover import Rover


def assert_rover_state(
    rover: Rover, x: float, y: float, faced_direction: CardinalPoint
):
    assert rover.position.x == x, f"Expected x:{x}, got {rover.position.x}"
    assert rover.position.y == y, f"Expected y:{y} on y, got {rover.position.y}"
    assert (
        rover.faced_direction == faced_direction
    ), f"Expected direction:{faced_direction}, got {rover.faced_direction}"
