import pytest

from mars_rover import CardinalPoint, Point, Rover
from tests.helpers import assert_rover_state


@pytest.mark.parametrize("x,y", [(0, 0), (0, 1), (3, 2), (6, 4)])
def test_rover_can_move_backward_when_facing_north_direction(x, y):
    rover = Rover(position=Point(x, y), direction=CardinalPoint.N)

    rover.move_backward()

    assert_rover_state(rover, x, y - 1, CardinalPoint.S)
