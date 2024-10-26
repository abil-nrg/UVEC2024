import pygame
class Tunnel:
    def __init__(self, x, y, size=50):
        self.x = x
        self.y = y
        self.size = size
    def get_area(self):
        return pygame.Rect(self.x, self.y, self.size, self.size)
