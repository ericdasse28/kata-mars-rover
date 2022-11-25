def assert_rover_state(rover, x, y, direction):
    assert rover.position.x == x
    assert rover.position.y == y
    assert rover.direction == direction
