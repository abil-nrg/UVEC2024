import pygame
from cat import Cat
from home import Home
from tunnel import Tunnel
from intersection import Intersection
from colours import *

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
cat = Cat(BLUE, 'r', 100, 50)
cat2 = Cat(RED, 'r', 130, 50)
home = Home(BLUE, 150, 50)

cats = [cat, cat2]
homes = [home]


# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(WHITE)
    pygame.draw.rect(screen, GREY, tunnel.get_area())
    for cat in cats:
        pygame.draw.circle(screen, cat.colour, (cat.x, cat.y), cat.size)
    for home in homes:
        pygame.draw.rect(screen, home.colour, home.get_area())
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    # --- Limit to 60 frames per second
    clock.tick(60)
# Close the window and quit.
pygame.quit()