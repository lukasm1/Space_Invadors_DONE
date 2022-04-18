from turtle import Turtle
import winsound


class Laser(Turtle):
    def __init__(self, shape):
        super().__init__()
        self.penup()
        self.shape(shape)
        self.goto(-1000, -1000)
        self.y_move = 10
        self.move_speed = 0.2

    def move(self):
        new_x = self.xcor()
        new_y = self.ycor()
        new_y += self.y_move
        self.goto(new_x, new_y)

    def disappear(self):
        self.goto(-1000, -1000)

    def shoot(self, x, y):
        if not self.ycor() < 300 or not self.ycor() > -300:
            winsound.PlaySound("./sounds/laser_sound.wav", winsound.SND_ASYNC)
            self.move_speed = 0.01
            self.goto(x, y)
