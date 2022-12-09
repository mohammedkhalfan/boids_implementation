# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 16:56:38 2022

@author: mk5636
"""
import random
import math
from PIL import Image, ImageTk


class Predator:
    def __init__(self, label):
        self.x = random.randrange(0, 400)
        self.y = 1
        self.angle = random.uniform(0.0, 2.0 * math.pi)
        self.label = label
        self.color = "red"

    def draw_boid(self, canvas):

        size = 18
        x1 = self.x + size * math.cos(self.angle)
        x2 = self.y + size * math.sin(self.angle)
        canvas.create_line(self.x, self.y, x1, x2, fill='red', arrow='both', arrowshape=(12.8,16,4.8), width=2, tags=self.label)

    def flock(self, canvas, screen_size, predator_speed):
        distance = predator_speed
        # calculate next the drone moves to
        if max(self.y, self.x) + distance >= screen_size:
            distance = -distance
            
        self.x += distance * math.cos(self.angle)
        self.y += distance * math.sin(self.angle)

        canvas.delete(self.label)
        self.draw_boid(canvas)

    def euclidean_distance(self, neighbour_boid):
        return math.sqrt((self.x - neighbour_boid.x) * (self.x - neighbour_boid.x) + \
                         (self.y - neighbour_boid.y) * (self.y - neighbour_boid.y))
