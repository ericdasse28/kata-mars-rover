from rover import Rover


class RoverCommands:
    """Interface to send commands to a Mars rover

    The class constructor requires a rover
    """

    def __init__(self, rover: Rover):
        self.rover = rover
        self.reported_messages = []

    def operate(self, commands: str):
        """Operate commands sent to the rover

        Args:
            commands (str): character array of commands
        """
        command_dictionary = {
            "f": self.rover.move_forward,
            "b": self.rover.move_backward,
            "r": self.rover.turn_right,
            "l": self.rover.turn_left,
        }

        for command in commands:
            rover_operation = command_dictionary[command]
            former_rover_position = self.rover.position
            former_faced_direction = self.rover.faced_direction

            rover_operation()

            if (
                self.rover.position == former_rover_position
                and self.rover.faced_direction == former_faced_direction
            ):
                obstacle_position = self.rover.last_avoided_obstacle
                report_message = f"Obstacle detected at {obstacle_position}"
                self.reported_messages.append(report_message)
                break

    def last_reported_message(self):
        return self.reported_messages[-1]
