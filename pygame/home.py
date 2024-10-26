import pygame
class Home:
    def __init__(self, colour, x, y, size=40):
        self.colour = colour
        self.x = x
        self.y = y
        self.size = size
    def get_area(self):
        return pygame.Rect(self.x, self.y, self.size, self.size)