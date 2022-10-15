from turtle import Turtle
from laser import Laser


class Player(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shapesize(7, 7, 7)
        self.setheading(90)
        self.fillcolor("gray")
        self.position = position
        self.penup()
        self.goto(position)

    def move_right(self):
        new_x = self.xcor() + 20
        self.goto(new_x, self.ycor())

    def move_left(self):
        new_x = self.xcor() - 20
        self.goto(new_x, self.ycor())

    def missile_guidance(self, army):
        min_dist = self.distance(army[0])
        enemy_ship = army[0]
        for alien in army:
            if self.distance(alien) < min_dist:
                min_dist = self.distance(alien)
                enemy_ship = alien
        return min_dist, enemy_ship

    def fire(self, army, wall, scoreboard):
        laser = Laser((self.xcor(), self.ycor()))
        laser.fillcolor("green")
        # laser.forward(800)
        target, enemy = self.missile_guidance(army)
        if len(wall) == 0:
            laser.goto(x=self.xcor(), y=enemy.ycor())
            laser.hideturtle()
            for soldier in army:
                if laser.distance(soldier) < 100:
                    soldier.hideturtle()
                    army.remove(soldier)
                    scoreboard.update_score()
        else:
            for brick in wall:
                if abs(self.xcor() - brick.xcor()) <= 150:
                    laser.goto(brick.xcor(), brick.ycor())
                    laser.hideturtle()
                    brick.hideturtle()
                    wall.remove(brick)
                    break
                else:
                    laser.goto(x=self.xcor(), y=enemy.ycor())
                    laser.hideturtle()
                    for soldier in army:
                        if laser.distance(soldier) < 100:

                            try:
                                soldier.hideturtle()
                                army.remove(soldier)
                                scoreboard.update_score()
                            except ValueError:
                                pass
