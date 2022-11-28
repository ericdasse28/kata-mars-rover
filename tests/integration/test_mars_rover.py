import pytest

from position import CardinalPoint, Position
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
