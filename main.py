import functools
from turtle import Screen
from score import Score
from monsters import Monster
from ship import Ship
from monster_shot import MonsterShot
from laser import Laser
import time
import random

PADDLE_POSITION = [(0, -250)]

# Monsters and their shots:
monster_position_x = -260
monster_position_y = 0
all_monsters = []
monster_shots = []
colors = ["red", "orange", "yellow", "green"]

screen = Screen()

ufo = "./images/ufo.gif"
invador = "./images/invador.gif"
enemy = "./images/enemy.gif"
laser_shape = "./images/laser.gif"
ship_shape = './images/space_ship.gif'
fire = "./images/fire.gif"

shapes = [ufo, invador, enemy]

screen.register_shape(fire)
screen.register_shape(ship_shape)
screen.register_shape(laser_shape)
screen.register_shape(ufo)
screen.register_shape(invador)
screen.register_shape(enemy)

screen.setup(width=800, height=600)
screen.bgpic('./images/space_bg.png')
screen.title("Space Invadors Game")

screen.tracer(0)
screen.listen()

game = True

# winsound.PlaySound("./sounds/cinematic.wav", winsound.SND_ASYNC)

laser = Laser(laser_shape)
monster_shot = MonsterShot(fire)
monster_shots.append(monster_shot)
score = Score()
ship = Ship(PADDLE_POSITION[0], ship_shape)

# Create monster wall:
for shape in shapes:

    for _ in range(2):

        for _ in range(0, 8):
            monster = Monster((monster_position_x, monster_position_y), shape)
            monster_position_x = monster_position_x + 70
            all_monsters.append(monster)

        monster_position_y = monster_position_y + 50
        monster_position_x = -260

while game:
    screen.onkey(functools.partial(laser.shoot, ship.xcor(), ship.ycor()), "space")
    screen.onkey(ship.left, "Left")
    screen.onkey(ship.right, "Right")

    time.sleep(laser.move_speed)
    laser.move()

    for monster in all_monsters:
        # Check if the monster got hit:
        if laser.distance(monster) < 27:
            all_monsters.remove(monster)
            monster.destroy_monster()
            laser.disappear()
            score.user_point()

        monster.move()
        # Check if the ship got shot:
        for shot in monster_shots:
            shot.move()
            if ship.distance(shot) < 30:
                score.end_game()
                game = False
                time.sleep(1)

        # Reverse monsters if on the wall:
        if monster.xcor() < -360 or monster.xcor() > 360:
            for monster in all_monsters:
                monster.reverse()

        # Shoot from a random space invador ship:
        random_number = random.randint(1, 800)
        if random_number == 1:
            new = MonsterShot(fire)
            monster_shots.append(new)
            monster_shot.shoot(new, monster.xcor(), monster.ycor())

        # Check if we got invaded:
        if ship.distance(monster) < 30 or monster.ycor() <= -250:
            score.end_game()
            game = False

    # Check if all invadors destroyed:
    if score.user_score == 48:
        score.win_game()
        game = False

    screen.update()

screen.exitonclick()