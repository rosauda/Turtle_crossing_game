from turtle import Turtle

STARTING_POSITION = (0, -250)
MOVE_DISTANCE = 30

class Timmy(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def reset_position(self):
        self.goto(STARTING_POSITION)





