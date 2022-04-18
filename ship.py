from turtle import Turtle


class Ship(Turtle):
    def __init__(self, position, shp):
        super().__init__()
        self.create_ship(position, shp)

    def create_ship(self, position, shp):
        self.setheading(180)
        self.shape(shp)
        self.penup()
        self.goto(position)

    def right(self):
        if self.xcor() < 360:
            new_x = self.xcor() + 40
            self.goto(new_x, self.ycor())

    def left(self):
        if self.xcor() > -360:
            new_x = self.xcor() - 40
            self.goto(new_x, self.ycor())