from turtle import Turtle

X=610
Y=229
FONT=("Courier", 25, "bold")
ALIGNMENT="right"


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.user_lives = 1
        self.user_score= 0
        self.hideturtle()
        self.color("white")
        self.goto(X, Y)
        self.write(arg=f"Lives: {self.user_lives}\nScore: {self.user_score}", align=ALIGNMENT, font=FONT)
        self.create_frame()

    def create_frame(self):
        self.goto(-410, -310)
        self.setheading(0)
        self.pensize(5)
        self.pendown()
        self.forward(820)
        self.setheading(90)
        self.forward(620)
        self.setheading(180)
        self.forward(820)
        self.setheading(270)
        self.forward(620)
        self.penup()

    def life_less(self):
        self.user_lives -= 1
        self.update_score()

    def user_point(self):
        self.user_score += 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.create_frame()
        self.goto(X, Y)
        self.write(arg=f"Lives: {self.user_lives}\nScore: {self.user_score}", align=ALIGNMENT, font=FONT)

    def end_game(self):
        self.clear()
        self.create_frame()
        self.goto(0, 200)
        self.write(arg=f"GAME OVER\nYour Score: {self.user_score}", align=ALIGNMENT, font=("Courier", 30, "bold"))

    def win_game(self):
        self.clear()
        self.create_frame()
        self.goto(0, 200)
        self.write(arg=f"YOU WON!\nYour Score: {self.user_score}", align=ALIGNMENT, font=("Courier", 30, "bold"))