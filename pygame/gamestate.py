import pygame, json
class GameState:
    def __init__(self, cats, homes, intersections, tunnel, ticks_since_last_cat, time, roads):
        self.cats = cats
        self.homes = homes
        self.intersections = intersections
        self.tunnel = tunnel
        self.ticks_since_last_cat = ticks_since_last_cat
        self.time = time
        self.roads = roads

    def to_json(self):
        return [cat.to_json() for cat in self.cats]