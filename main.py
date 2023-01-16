from turtle import Screen
import time
from timmy import Timmy
from cars import Car
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.title("Please help timmy to cross the street")
screen.tracer(0)

timmy = Timmy()
car = Car()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(timmy.up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.car_move()

    # Detect collision with car
    if timmy.distance(car) < 20:
        scoreboard.game_over()
        game_is_on = False

    # Detect collision with wall
    if timmy.ycor() > 250:
        scoreboard.timmy_crossed()
        timmy.reset_position()

screen.exitonclick()

