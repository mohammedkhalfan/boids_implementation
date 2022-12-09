# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 16:56:38 2022

@author: mk5636
"""
import random
import math
from PIL import Image, ImageTk


class Boid:
    def __init__(self, label, p_vigilant, response_time_lower, response_time_upper):
        self.x = random.randrange(100, 400)
        self.y = random.randrange(100, 400)
        self.angle = random.uniform(0.0, 2.0 * math.pi)
        self.label = label
        self.color = "black"
        self.distance = .1
        self.alert_time = None
        if random.randrange(1, 100) < p_vigilant: # 20% chance boid is vigilant
            self.status = 'v'
            self.rt = 0
        else:
            self.status = 'f'
            # if the bird is a forager, set it's response time between 2-5s
            self.rt = random.randrange(response_time_lower, response_time_upper)
        
    def draw_boid(self, canvas, color='black'):
        size = 18
        x1 = self.x + size * math.cos(self.angle)
        x2 = self.y + size * math.sin(self.angle)
        
        if self.status == 'fl': color = 'green'
        if color == 'black' and self.status == 'v': color='blue'
        canvas.create_line(self.x, self.y, x1, x2, fill=color, arrow='last', arrowshape=(12.8,16,4.8), width=2, tags=self.label)

    def flock(self, canvas, screen_size, boid_max_speed, color='black'):
        distance = min(boid_max_speed, self.distance)
        # calculate next the drone moves to
        self.x += distance * math.cos(self.angle)
        self.y += distance * math.sin(self.angle)
        # when drone goes off screen, will come back from other side of screen
        #self.x = self.x % screen_size
        #self.y = self.y % screen_size
        canvas.delete(self.label)
        #self.draw_boid(canvas, color)
        if self.x < screen_size and self.y < screen_size:
            self.draw_boid(canvas, color)
        else:
            self.x = 99999999
            self.y = 99999999

    def euclidean_distance(self, neighbour_boid):
        return math.sqrt((self.x - neighbour_boid.x) * (self.x - neighbour_boid.x) + \
                         (self.y - neighbour_boid.y) * (self.y - neighbour_boid.y))
