from turtle import Turtle
SCREEN_H = 600

FONT_ALIGN = "center"
FONT = ("Courier", 20, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.l_score = 0
        self.r_score = 0
        self.goto(0, (SCREEN_H/2 - 30))
        self.hideturtle()
        self.display_score()

    def add_point(self, paddle):
        if paddle == "left":
            self.l_score += 1
        elif paddle == "right":
            self.r_score += 1
        self.clear()
        self.display_score()

    def display_score(self):
        self.write(f"Score:  {self.l_score} / {self.r_score}", align=FONT_ALIGN, font=FONT)

    def game_over(self):
        self.goto(0,0)
        text = "Game Over.\n"
        self.write(text, align=FONT_ALIGN, font=FONT)

