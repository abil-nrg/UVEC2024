import pygame, json
class Tunnel:
    def __init__(self, x, y, size=1):
        self.x = x
        self.y = y
        self.size = size
    def get_area(self):
        return pygame.Rect(self.x-self.size/2, self.y-self.size/2, self.size, self.size)
    def to_json(self):
        return json.dumps(self.__dict__)