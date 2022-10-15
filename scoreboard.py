from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.lives = 3
        self.score = 0
        self.wave = 1
        self.display_stats()

    def display_stats(self):
        self.clear()
        self.goto(-450, 480)
        self.write(f"lives :{self.lives}", align="center", font=("Courier", 30, "normal"))
        self.goto(0, 480)
        self.write(f"wave :{self.wave}", align="center", font=("Courier", 30, "normal"))
        self.goto(450, 480)
        self.write(f"score: {self.score}", align="center", font=("Courier", 30, "normal"))

    def update_lives(self):
        self.lives -= 1
        self.display_stats()

    def update_score(self):
        self.score += 60
        self.display_stats()

    def game_over(self):
        self.clear()
        self.goto(0, 430)
        self.write("GAME OVER", align="center", font=("Courier", 40, "normal"))

    def next_wave(self):
        self.wave += 1
        self.display_stats()

    def check_game_over(self):
        if self.lives <= 0:
            self.game_over()
            return True
