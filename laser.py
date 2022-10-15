from turtle import Turtle


class Laser(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=3, stretch_wid=0.1)
        self.setheading(90)
        self.position = position
        self.goto(position)
