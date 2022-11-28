"""This module tests that the rover can move forward whatever the direction it is facing"""

import mars
import pytest

from location import CardinalPoint, Position
from rover import Rover
from tests.helpers import assert_rover_state


@pytest.mark.parametrize("x,y", [(0, 0), (0, 1), (3, 2), (6, 4)])
def test_rover_can_move_forward_when_facing_north_direction(x, y):
    rover = Rover(position=Position(x, y), faced_direction=CardinalPoint.N)

    rover.move_forward()

    assert_rover_state(rover, x, y + 1, CardinalPoint.N)


@pytest.mark.parametrize("x,y", [(0, 0), (0, 1), (3, 2), (6, 4)])
def test_rover_can_move_forward_when_facing_south_direction(x, y):
    rover = Rover(position=Position(x, y), faced_direction=CardinalPoint.S)

    rover.move_forward()

    assert_rover_state(rover, x, y - 1, CardinalPoint.S)


@pytest.mark.parametrize("x,y", [(0, 0), (0, 1), (3, 2), (6, 4)])
def test_rover_can_move_forward_when_facing_east_direction(x, y):
    rover = Rover(position=Position(x, y), faced_direction=CardinalPoint.E)

    rover.move_forward()

    assert_rover_state(rover, x + 1, y, CardinalPoint.E)


@pytest.mark.parametrize("x,y", [(0, 0), (0, 1), (3, 2), (6, 4)])
def test_rover_can_move_forward_when_facing_west_direction(x, y):
    rover = Rover(position=Position(x, y), faced_direction=CardinalPoint.W)

    rover.move_forward()

    assert_rover_state(rover, x - 1, y, CardinalPoint.W)


@pytest.mark.parametrize(
    "initial_x,initial_y,direction,expected_x,expected_y",
    [
        (0, 3300000, CardinalPoint.N, 0, -3300000),
        (0, -3300000, CardinalPoint.S, 0, 3300000),
        (3300000, 0, CardinalPoint.E, -3300000, 0),
        (-3300000, 0, CardinalPoint.W, 3300000, 0),
    ],
)
def test_rover_wraps_when_reaching_planet_edge_while_moving_forward(
    initial_x, initial_y, direction, expected_x, expected_y
):
    rover = Rover(position=Position(initial_x, initial_y), faced_direction=direction)

    rover.move_forward()

    assert_rover_state(rover, expected_x, expected_y, direction)


@pytest.mark.parametrize(
    "initial_x,initial_y,direction,expected_x,expected_y",
    [
        (0, 3300000, CardinalPoint.S, 0, 3299999),
        (0, -3300000, CardinalPoint.N, 0, -3299999),
        (3300000, 0, CardinalPoint.W, 3299999, 0),
        (-3300000, 0, CardinalPoint.E, -3299999, 0),
    ],
)
def test_rover_doesnt_wrap_when_reaching_planet_edge_while_moving_forward_in_a_different_direction(
    initial_x, initial_y, direction, expected_x, expected_y
):
    rover = Rover(position=Position(initial_x, initial_y), faced_direction=direction)

    rover.move_forward()

    assert_rover_state(rover, expected_x, expected_y, direction)
