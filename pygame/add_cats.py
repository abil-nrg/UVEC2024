from cat import Cat
from home import Home
from tunnel import Tunnel
from intersection import Intersection
from gamestate import GameState
from colours import *

import numpy as np
import random
import time

tunnel = Tunnel(5, 5)
cat = Cat(BLUE, 'r', 4, 3)
cat2 = Cat(RED, 'd', 8, 6)
home = Home(BLUE, 10, 4)
intersection = Intersection(4, 2, ['r', 'd'], 'd')
time_since_last_cat = 0
Cats = []

accepted_colors = [BLUE, RED]

def update_cats(time_since_last_cat, tunnel_x, tunnel_y, Cats):
    rate = 2
    x = np.random.exponential(scale= rate) 
    
    if time_since_last_cat >= x:
        color = random.choice(accepted_colors)
        new_cat = Cat(color, 'r' , tunnel_x, tunnel_y)
        Cats.append(new_cat)
    else:
        time_since_last_cat += 1

    return time_since_last_cat , Cats

ctr = 0
while True:
    ctr += 1
    time_since_last_cat, Cats = update_cats(time_since_last_cat, 1, 1, Cats)
  
    time.sleep(1)