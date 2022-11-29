from position import Planet


def test_add_obstacle():
    planet = Planet()
    obstacle_x = 0
    obstacle_y = 1

    planet.add_obstacle(obstacle_x, obstacle_y)

    assert (obstacle_x, obstacle_y) in planet.obstacles_coordinates
