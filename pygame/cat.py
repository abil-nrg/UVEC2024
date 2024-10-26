import pygame
import json
class Cat:
    def __init__(self, colour, direction, x, y, size = 20):
        self.colour = colour
        self.direction = direction
        self.x = x
        self.y = y
        self.size = size
    def get_area(self):
        return pygame.Rect(self.x-self.size/2, self.y-self.size/2, self.size, self.size)
    def to_json(self):
        json.dumps(self.__dict__)