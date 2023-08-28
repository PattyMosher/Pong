from turtle import Turtle

SCREEN_H = 600

class Paddle(Turtle):


    def __init__(self,x_pos):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.penup()
        self.shapesize(5,1)
        self.goto(x_pos,0)

    def go_up(self):
        if self.ycor() < SCREEN_H/2 -50:
            self.goto(self.xcor(), self.ycor() + 25)

    def go_down(self):
        if self.ycor() > -SCREEN_H/2 + 50:
            self.goto(self.xcor(), self.ycor() - 25)


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.home()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 5
        self.y_move = 5

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x,new_y)

    def y_bounce(self):
        self.y_move *= -1


    def x_bounce(self):
        self.x_move *= -1


    def reset_position(self):
        self.goto(0,0)
        self.x_bounce()