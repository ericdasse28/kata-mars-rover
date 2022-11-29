import pytest

from position import CardinalPoint, Planet, Position
from rover import Rover
from rover_commands import RoverCommands
from tests.helpers import assert_rover_state


@pytest.mark.parametrize(
    "commands,new_x,new_y,new_direction",
    [
        ("f", 0, 1, CardinalPoint.N),
        ("b", 0, -1, CardinalPoint.S),
        ("ffb", 0, 1, CardinalPoint.S),
        ("ffffb", 0, 3, CardinalPoint.S),
        ("ffffffbfbbbbffff", 0, 0, CardinalPoint.S),
        ("r", 0, 0, CardinalPoint.E),
        ("l", 0, 0, CardinalPoint.W),
        ("lr", 0, 0, CardinalPoint.N),
        ("fblr", 0, 0, CardinalPoint.S),
        ("ffffffffrrrrrblfrl", -1, 7, CardinalPoint.S),
    ],
)
def test_mars_rover_commands(commands, new_x, new_y, new_direction):
    rover = Rover(position=Position(0, 0), faced_direction=CardinalPoint.N)
    rover_interface = RoverCommands(rover=rover)

    rover_interface.operate(commands)

    assert_rover_state(rover, new_x, new_y, new_direction)


@pytest.mark.parametrize(
    "obstacle_x,obstacle_y,command,initial_x,initial_y,initial_direction,expected_x,expected_y,expected_direction",
    [
        (1, 3, "fffrfbffffffffff", 0, 0, CardinalPoint.N, 0, 3, CardinalPoint.E),
        (3, 8, "fffrfbffffffffff", 2, 5, CardinalPoint.N, 2, 8, CardinalPoint.E),
        (1, 8, "ffflfbffffffffff", 2, 5, CardinalPoint.N, 2, 8, CardinalPoint.W),
        (2, 9, "brlfffflrffffffff", 2, 5, CardinalPoint.S, 2, 8, CardinalPoint.N),
    ],
)
def test_mars_rover_moves_aborts_the_sequence_after_moving_to_last_possible_point_when_it_meets_an_obstacle(
    obstacle_x,
    obstacle_y,
    command,
    initial_x,
    initial_y,
    initial_direction,
    expected_x,
    expected_y,
    expected_direction,
):
    mars = Planet()
    mars.add_obstacle(obstacle_x, obstacle_y)
    rover = Rover(
        position=Position(initial_x, initial_y, planet=mars),
        faced_direction=initial_direction,
    )
    rover_commands = RoverCommands(rover=rover)

    rover_commands.operate(command)

    assert_rover_state(rover, expected_x, expected_y, expected_direction)
