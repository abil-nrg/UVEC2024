import pygame
import time
from cat import Cat
from home import Home
from tunnel import Tunnel
from intersection import Intersection
from gamestate import GameState
from colours import *

# 0 <= x <= 12
# 0 <= y <= 9

tunnel = Tunnel(5, 5)
cat = Cat(BLUE, 'r', 4, 3)
cat2 = Cat(RED, 'd', 8, 6)
home = Home(BLUE, 10, 4)
intersection = Intersection(4, 2, ['r', 'd'], 'd')
time_since_last_cat = 0

cats = [cat, cat2]
homes = [home]
intersections = [intersection]

for cat in cats:
    for home in homes:
        if cat.get_area().colliderect(home.get_area()):
            if cat.colour == home.colour:
                cats.remove(cat)
            else:
                print("game end")
    for intersection in intersections:
        if cat.get_area().colliderect(intersection.get_area()):
            cat.direction = intersection.current_direction
    if cat.direction == 'r': cat.x += 1
    elif cat.direction == 'l': cat.x -= 1
    elif cat.direction == 'u': cat.y -= 1
    elif cat.direction == 'd': cat.y += 1

time_since_last_cat += 1