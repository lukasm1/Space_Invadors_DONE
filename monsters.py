from turtle import Turtle


class Monster(Turtle):
    def __init__(self, position, shape):
        super().__init__()
        self.create_monster(position, shape)

    def create_monster(self, position, shape):
        self.shape(shape)
        self.setheading(180)
        self.penup()
        self.goto(position)
        self.speed = -1

    def destroy_monster(self):
        self.sety(1000)

    def move(self):
        new_x = self.xcor()
        new_y = self.ycor()
        new_x += self.speed
        self.goto(new_x, new_y)

    def reverse(self):
        new_y = self.ycor()
        new_y += -20
        self.sety((new_y))
        self.speed *= -1