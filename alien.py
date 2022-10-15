import random
from turtle import Turtle, Screen
from laser import Laser


class Alien:
    def __init__(self):
        self.fleet = []

    def build_armada(self):
        starting_x = -400
        starting_y = 100
        for i in range(0, 3):
            starting_y += 100
            starting_x = -400
            for j in range(0, 7):
                starting_x += 100
                alien = Turtle()
                alien.fillcolor("green")
                alien.shape("turtle")
                alien.shapesize(3, 3, 3)
                alien.speed("fastest")
                alien.goto(starting_x, starting_y)
                self.fleet.append(alien)

    def move_fleet_forward(self):
        for alien in self.fleet:
            for i in range(0, 7):
                alien.speed("fastest")
                alien.forward(10)

    def move_fleet_backward(self):
        for alien in self.fleet:
            for i in range(0, 7):
                alien.speed("fastest")
                alien.backward(10)

    def swarm(self):
        for alien in self.fleet:
            alien.goto(random.randint(-300, 300), random.randint(100, 500))
            if alien.distance(alien) < 60:
                alien.forward(50)

    def has_shot(self, cors):
        min_dist = self.fleet[0].distance(cors)
        for alien in self.fleet:
            if alien.distance(cors) < min_dist:
                min_dist = alien.distance(cors)
        for alien in self.fleet:
            if min_dist == alien.distance(cors):
                return min_dist, alien

    def attack(self, attack_cors, wall, scoreboard):
        target, shooter = self.has_shot(attack_cors)
        x_cor = shooter.xcor()
        y_cor = shooter.ycor() + 50
        laser = Laser((x_cor, y_cor))
        laser.fillcolor("red")
        laser.penup()
        if len(wall) != 0:
            for brick in wall[::-1]:
                if not scoreboard.check_game_over():
                    if abs(laser.xcor() - brick.xcor()) <= 300:
                        laser.goto(brick.xcor(), brick.ycor())
                        laser.hideturtle()
                        brick.hideturtle()
                        try:
                            wall.remove(brick)
                            break
                        except ValueError:
                            pass
                    else:
                        laser.goto(laser.xcor(), attack_cors.ycor())
                        laser.hideturtle()
                        if laser.distance(attack_cors) < 80:
                            attack_cors.hideturtle()
                            scoreboard.update_lives()
                            attack_cors.goto(x=0, y=-400)
                            attack_cors.showturtle()
                            break

                else:
                    break

        else:
            laser.goto(shooter.xcor(), attack_cors.ycor())
            laser.hideturtle()
            if laser.distance(attack_cors) < 100:
                attack_cors.hideturtle()
                scoreboard.update_lives()
                attack_cors.goto(x=0, y=-400)
                attack_cors.showturtle()
