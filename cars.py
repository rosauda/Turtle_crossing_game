import random
from turtle import Turtle
from timmy import Timmy
from scoreboard import Scoreboard

colors = ["red", "blue", "green", "black", "yellow", "brown", "purple"]


class Car(Turtle):

    def __init__(self):
        super().__init__()
        self.color(random.choice(colors))
        self.shape("square")
        self.shapesize(stretch_wid=2, stretch_len=1)
        self.penup()
        self.goto(450, 0)
        self.setheading(90)

    def car_move(self):
        new_x = self.xcor() - 10
        self.goto(new_x, self.ycor())

