from turtle import Turtle


class MonsterShot(Turtle):
    def __init__(self, fire):
        super().__init__()
        self.penup()
        self.shapesize(1)
        self.shape(fire)
        self.goto(-1000, -1000)
        self.y_move = -0.2
        self.move_speed = 0

    def move(self):
        new_y = self.ycor()
        new_y += self.y_move
        self.sety(new_y)

    def disappear(self):
        self.goto(-1000, -1000)

    def shoot(self, new, x, y):
            new.move_speed = 0.000001
            new.goto(x, y)