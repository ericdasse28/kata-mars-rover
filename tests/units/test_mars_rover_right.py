import pytest

from location import CardinalPoint, Position
from mars_rover import Rover
from tests.helpers import assert_rover_state


@pytest.mark.parametrize("x,y", [(0, 0), (0, 1), (3, 2), (6, 4)])
def test_rover_can_turn_right_when_facing_north_direction(x, y):
    rover = Rover(position=Position(x, y), faced_direction=CardinalPoint.N)

    rover.turn_right()

    assert_rover_state(rover, x + 1, y, CardinalPoint.E)


@pytest.mark.parametrize("x,y", [(0, 0), (0, 1), (3, 2), (6, 4)])
def test_rover_can_turn_right_when_facing_south_direction(x, y):
    rover = Rover(position=Position(x, y), faced_direction=CardinalPoint.S)

    rover.turn_right()

    assert_rover_state(rover, x - 1, y, CardinalPoint.W)


@pytest.mark.parametrize("x,y", [(0, 0), (0, 1), (3, 2), (6, 4)])
def test_rover_can_turn_right_when_facing_east_direction(x, y):
    rover = Rover(position=Position(x, y), faced_direction=CardinalPoint.E)

    rover.turn_right()

    assert_rover_state(rover, x, y - 1, CardinalPoint.S)


@pytest.mark.parametrize("x,y", [(0, 0), (0, 1), (3, 2), (6, 4)])
def test_rover_can_turn_right_when_facing_west_direction(x, y):
    rover = Rover(position=Position(x, y), faced_direction=CardinalPoint.W)

    rover.turn_right()

    assert_rover_state(rover, x, y + 1, CardinalPoint.N)
