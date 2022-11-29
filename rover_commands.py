from rover import Rover


class RoverCommands:
    """Interface to send commands to a Mars rover

    The class constructor requires a rover
    """

    def __init__(self, rover: Rover):
        self.rover = rover

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
                break
