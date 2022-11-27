import pytest

from mars_rover import CardinalPoint, Point, Rover
from mars_rover_interface import RoverInterface
from tests.helpers import assert_rover_state


@pytest.mark.parametrize(
    "commands,new_x,new_y,new_direction",
    [
        ("f", 0, 1, CardinalPoint.N),
        ("b", 0, -1, CardinalPoint.S),
        ("ffb", 0, 1, CardinalPoint.S),
        ("ffffb", 0, 3, CardinalPoint.S),
        ("ffffffbfbbbbffff", 0, 0, CardinalPoint.S),
    ],
)
def test_mars_rover_commands(commands, new_x, new_y, new_direction):
    rover = Rover(position=Point(0, 0), direction=CardinalPoint.N)
    rover_interface = RoverInterface(rover=rover)

    rover_interface.operate(commands)

    assert_rover_state(rover, new_x, new_y, new_direction)
