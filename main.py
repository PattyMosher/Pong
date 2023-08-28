#Pong Game
from turtle import Screen
from paddle import Paddle, Ball
from scoreboard import ScoreBoard
import time

SCREEN_H = 600
SCREEN_W =800
L_X = -350
R_X = 350

screen = Screen()
screen.setup(SCREEN_W,SCREEN_H)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
screen.listen()


r_paddle = Paddle(R_X)
l_paddle = Paddle(L_X)
ball = Ball()
score = ScoreBoard()



screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


game_on = True
speed = .05
while game_on:
    screen.update()
    ball.move()
    time.sleep(speed)
    #bounce off the wall, reverse y direction
    if ball.ycor() > SCREEN_H/2 - 10 or ball.ycor() <= -SCREEN_H/2 + 2:
        ball.y_bounce()
    #bounce off right paddle, reverse x direction
    elif ball.distance(r_paddle) < 50 and ball.xcor() == R_X -20:
        ball.x_bounce()
    #bounce off left paddle
    elif ball.distance(l_paddle) < 50 and ball.xcor() == L_X + 20:
        ball.x_bounce()

    # if a player misses, the other gets a point and the ball is reset
    elif ball.xcor() > R_X:
        score.add_point("left")
        ball.reset_position()

    elif ball.xcor() < L_X:
        score.add_point("right")
        ball.reset_position()

    # game ends at 10 points
    if score.l_score == 10 or score.r_score == 10:
        score.game_over()
        game_on = False




screen.exitonclick()