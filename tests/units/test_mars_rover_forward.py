"""This module tests that the rover can move forward whatever the direction it is facing"""

import pytest

from position import CardinalPoint, Position, Planet
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


@pytest.mark.parametrize(
    "obstacle_x,obstacle_y,rover_x,rover_y",
    [
        (0, 1, 0, 0),
        (0, 2, 0, 1),
        (6, 5, 6, 4),
        (8, 6, 8, 5),
    ],
)
def test_rover_doesnt_move_forward_when_there_is_an_obstacle_infront_of_it_while_facing_north(
    obstacle_x, obstacle_y, rover_x, rover_y
):
    mars = Planet()
    mars.add_obstacle(obstacle_x, obstacle_y)
    rover = Rover(
        position=Position(rover_x, rover_y, planet=mars),
        faced_direction=CardinalPoint.N,
    )

    rover.move_forward()

    assert_rover_state(rover, rover_x, rover_y, CardinalPoint.N)


@pytest.mark.parametrize(
    "obstacle_x,obstacle_y,rover_x,rover_y",
    [
        (0, -1, 0, 0),
        (0, 0, 0, 1),
        (6, 3, 6, 4),
        (8, 4, 8, 5),
    ],
)
def test_rover_doesnt_move_forward_when_there_is_an_obstacle_infront_of_it_while_facing_south(
    obstacle_x, obstacle_y, rover_x, rover_y
):
    mars = Planet()
    mars.add_obstacle(obstacle_x, obstacle_y)
    rover = Rover(
        position=Position(rover_x, rover_y, planet=mars),
        faced_direction=CardinalPoint.S,
    )

    rover.move_forward()

    assert_rover_state(rover, rover_x, rover_y, CardinalPoint.S)


@pytest.mark.parametrize(
    "obstacle_x,obstacle_y,rover_x,rover_y",
    [
        (1, 0, 0, 0),
        (1, 1, 0, 1),
        (7, 4, 6, 4),
        (9, 5, 8, 5),
    ],
)
def test_rover_doesnt_move_forward_when_there_is_an_obstacle_infront_of_it_while_facing_east(
    obstacle_x, obstacle_y, rover_x, rover_y
):
    mars = Planet()
    mars.add_obstacle(obstacle_x, obstacle_y)
    rover = Rover(
        position=Position(rover_x, rover_y, planet=mars),
        faced_direction=CardinalPoint.E,
    )

    rover.move_forward()

    assert_rover_state(rover, rover_x, rover_y, CardinalPoint.E)


@pytest.mark.parametrize(
    "obstacle_x,obstacle_y,rover_x,rover_y",
    [
        (-1, 0, 0, 0),
        (-1, 1, 0, 1),
        (5, 4, 6, 4),
        (7, 5, 8, 5),
    ],
)
def test_rover_doesnt_move_forward_when_there_is_an_obstacle_infront_of_it_while_facing_west(
    obstacle_x, obstacle_y, rover_x, rover_y
):
    mars = Planet()
    mars.add_obstacle(obstacle_x, obstacle_y)
    rover = Rover(
        position=Position(rover_x, rover_y, planet=mars),
        faced_direction=CardinalPoint.W,
    )

    rover.move_forward()

    assert_rover_state(rover, rover_x, rover_y, CardinalPoint.W)


@pytest.mark.parametrize(
    "initial_rover_x,initial_rover_y,direction,obstacle_x,obstacle_y",
    [
        (0, 3300000, CardinalPoint.N, 0, -3300000),
        (0, -3300000, CardinalPoint.S, 0, 3300000),
        (3300000, 0, CardinalPoint.E, -3300000, 0),
        (-3300000, 0, CardinalPoint.W, 3300000, 0),
    ],
)
def test_rover_doesnt_wrap_when_moving_forward_while_there_is_an_obstacle_at_the_next_position(
    initial_rover_x, initial_rover_y, direction, obstacle_x, obstacle_y
):
    mars = Planet()
    mars.add_obstacle(obstacle_x, obstacle_y)
    rover = Rover(
        position=Position(initial_rover_x, initial_rover_y, planet=mars),
        faced_direction=direction,
    )

    rover.move_forward()

    assert_rover_state(rover, initial_rover_x, initial_rover_y, direction)
