from cat import Cat
from home import Home
from tunnel import Tunnel
from intersection import Intersection
from gamestate import GameState
from colours import *


tunnel = Tunnel(50, 50)
cat = Cat(BLUE, 'r', 50, 50)
cat2 = Cat(RED, 'd', 130, 50)
home = Home(BLUE, 1000, 50)
intersection = Intersection(800, 50, ['r', 'd'], 'd')

cats = [cat, cat2]
homes = [home]
intersections = [intersection]

state = GameState(cats, homes, intersections, tunnel, 50, 40, [])
print(cats.to)
