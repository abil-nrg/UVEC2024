class Intersection:
    def __init__(self, x, y, possible_direction, current_direction, user=None):
        self.x = x
        self.y = y
        self.possible_direction = possible_direction
        self.current_direction = current_direction
        self.user = user
    def click(self):
        self.possible_direction[self.possible_direction.index(self.current_direction) + 1 % len(self.possible_direction)]
