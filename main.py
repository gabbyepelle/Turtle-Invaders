from turtle import Turtle, Screen
from player import Player
from alien import Alien
from scoreboard import Scoreboard
from laser import Laser
from barrier import Barrier
from space import Space
from functools import partial


# ----------------Functions----------------------------------#


def build_barrier():
    wall = []
    start_x = -300
    start_y = -200

    for i in range(0, 3):
        start_y += 20
        start_x = -300
        for j in range(0, 3):
            barrier = Barrier((start_x, start_y))
            start_x += 300
            wall.append(barrier)
    return wall


# --------------------------------------------------------------#
screen = Screen()
screen.setup(width=1300, height=2000)
screen.bgcolor("black")
screen.title("Space Invaders")
space = Space()
player = Player((0, -400))
alien = Alien()
army = alien.fleet
alien.build_armada()
wall = build_barrier()
scoreboard = Scoreboard()
scoreboard.display_stats()

screen.onkey(player.move_left, "Left")
screen.onkey(player.move_right, "Right")

screen.onkey(partial(player.fire, army, wall, scoreboard), "space")
screen.listen()

while True:

    if not scoreboard.check_game_over():
        #alien.move_fleet_forward()
        alien.attack(player, wall, scoreboard)
        alien.swarm()
        #alien.rain_fire(player, scoreboard, wall)
        #alien.move_fleet_backward()
        if len(army) == 0:
            scoreboard.next_wave()
            player.goto(0, -400)
            if len(wall) > 0:
                del wall
            wall = build_barrier()
            alien.build_armada()
    else:
        break

turtle.mainloop()
