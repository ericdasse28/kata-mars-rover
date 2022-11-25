import pytest
from mars_rover import Point, Rover


@pytest.mark.parametrize("x,y", [(0, 0), (0, 1), (3, 2), (6, 4)])
def test_rover_can_move_forward_when_facing_north_direction(x, y):
    rover = Rover(position=Point(x, y), direction="N")

    rover.move_forward()

    assert_rover_state(rover, x, y + 1, "N")


def test_rover_can_move_forward_when_facing_south_direction():
    rover = Rover(position=Point(0, 0), direction="S")

    rover.move_forward()

    assert_rover_state(rover, 0, -1, "S")


def assert_rover_state(rover, x, y, direction):
    assert rover.position.x == x
    assert rover.position.y == y
    assert rover.direction == direction
