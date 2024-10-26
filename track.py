import pygame

class Track:
    def __init__(self):
        self.track_images = {
            "horizontal": pygame.image.load("./img/track_horizontal.png"),
            "vertical": pygame.image.load("./img/track_vertical.png"),
            "corner_top_left": pygame.image.load("./img/track_corner_top_left.png"),
            "corner_top_right": pygame.image.load("./img/track_corner_top_right.png"),
            "corner_bottom_left": pygame.image.load("./img/track_corner_bottom_left.png"),
            "corner_bottom_right": pygame.image.load("./img/track_corner_bottom_right.png"),
        }

    def draw_track(self, screen, track_type, x, y):
        if track_type in self.track_images:
            screen.blit(self.track_images[track_type], (x, y))
        else:
            print(f"Track type '{track_type}' not found.")
