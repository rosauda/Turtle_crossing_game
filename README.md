Turtle crossing game:

the goal is to help the turtle to cross a busy stree.

1. A turtle moves forward when pressing the arrow up key. (it can only move forward)
2. Cars are randomly generated and will move from the right edge of the screen to the left edge
3. When the turtle crosses the street without being hit by a car, it moves back to the original position and the player levels up
4. When the turtle collides with a car, it`s game over

Problem breakdown:

1. Create a turtle player that starts at the bottom of the screen and listen for the "Up" keypress to move the turtle north
2. Create cars that are 20px high by 40px wide that are randomly generated along the y-axis and move to the left edge of the screen
3. Detect when the turtle player collides with a car and stop the game if this happens.
4. Detect when the turtle player has reached the top edge of the screen (i.e., reached the FINISH_LINE_Y). When this happens, return the turtle to the starting position and increase the speed of the cars
5. Create a scoreboard that keeps track of which level the user is on. Every time the turtle player does a successful crossing, the level should increase. When the turtle hits a car, GAME OVER should be displayed in the centre.