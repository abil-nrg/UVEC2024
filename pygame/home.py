import pygame, json
class Home:
    def __init__(self, colour, x, y, size=1):
        self.colour = colour
        self.x = x
        self.y = y
    def get_area(self):
        return pygame.Rect(self.x-self.size/2, self.y-self.size/2, self.size, self.size)
    def to_json(self):
        return json.dumps(self.__dict__)