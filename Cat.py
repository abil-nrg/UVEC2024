import pygame
import random
from colours import *  
class Cat:
    def __init__(self, colour, direction, x, y):
        self.colour = colour
        self.direction = direction
        self.x = x
        self.y = y
    def load_image(self):
        image_path = f"./images/cat_{self.colour}.png"
        try:
            image = pygame.image.load(image_path)
            return image
        except pygame.error:
            print(f"Could not load image for colour: {self.colour}")
            return None

    def draw(self, screen):
        if self.image:
            screen.blit(self.image, (self.x, self.y))

class Cat:

    COLORS = [WHITE, BLACK, DARK_RED, RED, DARK_BLUE, BLUE, GREY, DARK_GREY, WALL_BROWN, PURPLE, MAGENTA, LIGHT_GREEN, LIGHTER_GREEN, GOLD]

    def __init__(self, colour=None, direction="right", x=0, y=0):
        self.colour = colour if colour else random.choice(self.AVAILABLE_COLORS)
        self.direction = direction
        self.x = x
        self.y = y
        self.body_radius = 30
        self.head_radius = 20

    def draw(self, screen):
        pygame.draw.circle(screen, self.colour, (self.x, self.y), self.body_radius)

        head_x = self.x
        head_y = self.y - self.body_radius - self.head_radius + 10  
        pygame.draw.circle(screen, self.colour, (head_x, head_y), self.head_radius)

        ear_offset = 10
        ear_size = 10 

        left_ear_points = [
            (head_x - ear_offset, head_y - self.head_radius),
            (head_x - ear_offset - ear_size, head_y - ear_size),
            (head_x - ear_offset + ear_size, head_y - ear_size)
        ]
        pygame.draw.polygon(screen, self.colour, left_ear_points)

        right_ear_points = [
            (head_x + ear_offset, head_y - self.head_radius),  
            (head_x + ear_offset - ear_size, head_y - ear_size), 
            (head_x + ear_offset + ear_size, head_y - ear_size)
        ]
        pygame.draw.polygon(screen, self.colour, right_ear_points)

