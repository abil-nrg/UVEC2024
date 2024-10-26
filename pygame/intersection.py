import pygame, json
class Intersection:
    def __init__(self, x, y, possible_direction, current_direction, user=None, size=40):
        self.x = x
        self.y = y
        self.possible_direction = possible_direction
        self.current_direction = current_direction
        self.user = user
        self.size = size
    def get_drawn_area(self):
        return pygame.Rect(self.x-self.size/2, self.y-self.size/2, self.size, self.size)
    def get_area(self):
        return pygame.Rect(self.x, self.y, 1, 1)
    def click(self):
        self.possible_direction[self.possible_direction.index(self.current_direction) + 1 % len(self.possible_direction)]
    def to_json(self):
        return json.dumps(self.__dict__)