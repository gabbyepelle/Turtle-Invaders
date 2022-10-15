import turtle
from turtle import Turtle
import random


class Space(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.speed("fastest")
        self.penup()
        for i in range(30):
            self.goto(x=random.randint(-650, 650), y=random.randint(-500, 500))
            self.dot(1, "white")
            self.dot(2, "white")
