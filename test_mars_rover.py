import pytest
from mars_rover import CardinalPoint, Point, Rover


@pytest.mark.parametrize("x,y", [(0, 0), (0, 1), (3, 2), (6, 4)])
def test_rover_can_move_forward_when_facing_north_direction(x, y):
    rover = Rover(position=Point(x, y), direction=CardinalPoint.N)

    rover.move_forward()

    assert_rover_state(rover, x, y + 1, CardinalPoint.N)


@pytest.mark.parametrize("x,y", [(0, 0), (0, 1), (3, 2), (6, 4)])
def test_rover_can_move_forward_when_facing_south_direction(x, y):
    rover = Rover(position=Point(x, y), direction=CardinalPoint.S)

    rover.move_forward()

    assert_rover_state(rover, x, y - 1, CardinalPoint.S)


def assert_rover_state(rover, x, y, direction):
    assert rover.position.x == x
    assert rover.position.y == y
    assert rover.direction == direction
