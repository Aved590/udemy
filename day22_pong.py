from turtle import Screen
from day22_class import Paddle, Ball, Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title = "Pong"
screen.tracer(0)
ball_speed = 0.1


r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()
scoreboard.update_scoreboard()


screen.listen()
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

game_on = True
while game_on:
    time.sleep(ball_speed)
    screen.update()
    ball.move()

    # Detect top and bottom wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        #print("Out")
        ball.bounce_y()

    # Detect collision with  paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()



screen.exitonclick()
