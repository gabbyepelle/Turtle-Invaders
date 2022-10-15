from turtle import Turtle


class Barrier(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=6)
        self.fillcolor("white")
        self.speed("fastest")
        self.penup()
        self.position = position
        self.goto(position)
