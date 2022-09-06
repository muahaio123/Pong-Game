from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# set up screen and make it listen to input
scr = Screen()
scr.setup(width=800, height=600)
scr.bgcolor("black")
scr.title("PONG")
scr.listen()
scr.tracer(0)

# draw the line in the middle
mid_line = Turtle()
mid_line.hideturtle()
mid_line.color("white")
mid_line.width(5)
mid_line.setheading(270)
mid_line.speed(0)
mid_line.penup()
mid_line.goto(x=0, y=285)
curr_pen = "up"

for line_num in range(19):
    if curr_pen == "up":
        mid_line.pendown()
        curr_pen = "down"
    else:
        mid_line.penup()
        curr_pen = "up"

    mid_line.forward(30)

# create left and right paddle and assign keybind to it
l_paddle = Paddle(x_cor=-350, y_cor=0)
r_paddle = Paddle(x_cor=350, y_cor=0)

scr.onkeypress(fun=r_paddle.go_up, key="Up")
scr.onkeypress(fun=r_paddle.go_down, key="Down")

scr.onkeypress(fun=l_paddle.go_up, key="w")
scr.onkeypress(fun=l_paddle.go_down, key="s")

# create scoreboard
sc_board = Scoreboard()

ball = Ball()

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    scr.update()
    ball.move()

    # detect collision with upper and below wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with paddle:
    if (ball.distance(r_paddle) < 60 and 350 > ball.xcor() > 340) or (ball.distance(l_paddle) < 60 and (
            -340 > ball.xcor() > -350)):
        ball.bounce_x()

    # detect collision with left wall: score for right side
    if ball.xcor() < -390:
        sc_board.r_point()
        ball.reset_pos()
        ball.ball_right()

    # detect collision with right wall: score for left side
    elif ball.xcor() > 390:
        sc_board.l_point()
        ball.reset_pos()
        ball.ball_left()



scr.exitonclick()
