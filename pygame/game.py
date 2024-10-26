import pygame
from cat import Cat
from home import Home
from tunnel import Tunnel
from intersection import Intersection
from colours import *
import json

pygame.init()

screen_width = 1440
screen_height = 810
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Homeless kitties')

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

tunnel = Tunnel(50, 50)
cat = Cat(BLUE, 'r', 50, 50)
cat2 = Cat(RED, 'd', 130, 50)
home = Home(BLUE, 1000, 50)
intersection = Intersection(800, 50, ['r', 'd'], 'd')

cats = [cat, cat2]
homes = [home]
intersections = [intersection]

cat_json = [cat.to_json() for cat in cats]
homes_json = [home.to_json() for home in homes]
intersection_json = [intersection.to_json() for intersection in intersections]
tunnel = tunnel.to_json()

print(cat_json)
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # screen.fill(WHITE)
    # pygame.draw.rect(screen, GREY, tunnel.get_area())

    # for home in homes:
    #     pygame.draw.rect(screen, home.colour, home.get_area())

    # for intersection in intersections:
    #     pygame.draw.rect(screen, DARK_RED, intersection.get_drawn_area())

    # for cat in cats:
    #     pygame.draw.circle(screen, cat.colour, (cat.x, cat.y), cat.size)
    #     for home in homes:
    #         if cat.get_area().colliderect(home.get_area()):
    #             print("collide")
    #             cats.remove(cat)
    #     for intersection in intersections:
    #         if cat.get_area().colliderect(intersection.get_area()):
    #             print('intersect')
    #             cat.direction = intersection.current_direction
    #     if cat.direction == 'r': cat.x += 10
    #     elif cat.direction == 'l': cat.x -= 10
    #     elif cat.direction == 'u': cat.y -= 10
    #     elif cat.direction == 'd': cat.y += 10

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    # --- Limit to 6 frames per second
    clock.tick(60)
# Close the window and quit.
pygame.quit()