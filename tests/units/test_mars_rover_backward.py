import pytest

from location import CardinalPoint, Position
from mars_rover import Rover
from tests.helpers import assert_rover_state


@pytest.mark.parametrize("x,y", [(0, 0), (0, 1), (3, 2), (6, 4)])
def test_rover_can_move_backward_when_facing_north_direction(x, y):
    rover = Rover(position=Position(x, y), faced_direction=CardinalPoint.N)

    rover.move_backward()

    assert_rover_state(rover, x, y - 1, CardinalPoint.S)


@pytest.mark.parametrize("x,y", [(0, 0), (0, 1), (3, 2), (6, 4)])
def test_rover_can_move_backward_when_facing_south_direction(x, y):
    rover = Rover(position=Position(x, y), faced_direction=CardinalPoint.S)

    rover.move_backward()

    assert_rover_state(rover, x, y + 1, CardinalPoint.N)


@pytest.mark.parametrize("x,y", [(0, 0), (0, 1), (3, 2), (6, 4)])
def test_rover_can_move_backward_when_facing_east_direction(x, y):
    rover = Rover(position=Position(x, y), faced_direction=CardinalPoint.E)

    rover.move_backward()

    assert_rover_state(rover, x - 1, y, CardinalPoint.W)


@pytest.mark.parametrize("x,y", [(0, 0), (0, 1), (3, 2), (6, 4)])
def test_rover_can_move_backward_when_facing_south_direction(x, y):
    rover = Rover(position=Position(x, y), faced_direction=CardinalPoint.W)

    rover.move_backward()

    assert_rover_state(rover, x + 1, y, CardinalPoint.E)


def test_rover_doesnt_wrap_when_reaching_planet_edge_while_moving_backward_and_facing_north():
    rover = Rover(position=Position(0, 3300000), faced_direction=CardinalPoint.N)

    rover.move_backward()

    assert_rover_state(rover, 0, 3299999, CardinalPoint.S)


def test_rover_wraps_when_reaching_planet_edge_while_moving_forward_and_facing_south():
    rover = Rover(position=Position(0, 3300000), faced_direction=CardinalPoint.S)

    rover.move_backward()

    assert_rover_state(rover, 0, -3300000, CardinalPoint.N)
