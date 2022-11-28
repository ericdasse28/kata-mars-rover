# Kata Mars Rover
The goal of this kata is to develop an API that translates the commands sent from earth to instructions that are
understood by the rover. This solution is based on the requirements and rules specified at https://kata-log.rocks/mars-rover-kata

## Assumptions
Since a lot of things were not specified more precisely in the requirements and rules of the kata (at least
the kata as stated on the aforementioned link), I made some assumptions

### Position assumptions

1. Going in the north direction corresponds to moving towards the positive part of the y-axis
2. Going south is similar but towards the negative part of y-axis
3. Going to the east is going towards the positive part of the x-axis
4. Going to the west is going towards the negative part of the x-axis

### Movement assumptions
1. Moving forward is going towards the direction we are facing while incrementing or
decrementing the corresponding axis (Ex. Moving towards the north increments the y value by 1, moving towards the west decrements the x value by 1)
2. Moving backward consist in first facing the opposite direction and then moving towards that direction while incrementing or decrementing the corresponding axis value
3. Turning right simply consists in facing the direction on the right of the currently faced direction
4. Turning left is analogous to turning right

### Surface assumptions
1. The rover moves on a square
2. When the rover reaches an edge, and tries to go further, it appears on the other side of the square
while facing the same direction