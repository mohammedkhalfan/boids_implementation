# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 16:55:18 2022

@author: mk5636
"""
import tkinter
import random
import math
import Boid, Predator
import numpy as np

## PARAMETERS
no_of_boids = 40
predator_speed = 3.3
detection_range = 100
p_vigilant = 20
response_time_lower = 11
response_time_upper = 25
boid_max_speed = 3
acceleration_param = 10
p_catch_prey = 90
screen_size = 400


def initialise_canvas(window, screen_size):
    canvas = tkinter.Canvas(window, width=screen_size, height=screen_size)
    canvas.pack()
    window.resizable(False, False)
    return canvas

def create_boids(canvas, no_of_boids, p_vigilant, response_time_lower, response_time_upper):
    list_of_boids = []
    for n in range(no_of_boids):
        boid = Boid.Boid("boid" + str(n), p_vigilant, response_time_lower, response_time_upper)
        list_of_boids.append(boid)
        boid.draw_boid(canvas)
    return list_of_boids

def create_predator(canvas):
    predator = Predator.Predator("predator")
    predator.draw_boid(canvas)
    return predator

def avoidance(predator, boid, t):
    if boid.alert_time is None:
        boid.alert_time = t
    if boid.status != 'fl':
        boid.status = 'fl'
    #boid.distance = boid_max_speed
    boid.distance = (t - (boid.alert_time + boid.rt)) * boid_max_speed/acceleration_param
    # calculate current next distance, if it will be greater than now, don't change
    # it, if it will be less, then use predator.angle? 
    l = np.arange(-3.14, 3.14, .01)
    max_d = 0
    angle = None
    for i in l:
        boid_x = boid.x + boid.distance * math.cos(i)
        boid_y = boid.y + boid.distance * math.sin(i)
        d = math.sqrt((predator.x - boid_x) * (predator.x - boid_x) + \
                      (predator.y - boid_y) * (predator.y - boid_y))
        if d > max_d:
            max_d = d
            angle = i
            
    if angle is not None:
        boid.angle = angle*.7 + boid.angle*.3
    else:
        print("angle is none")
    
    
    #boid.angle = (predator.angle)

def separation(nearest_neighbour, boid):
    # move 1: move away from nearest - separation
    # calculate angle between boid and nearest boid, then angle it in the opposite direction
    if nearest_neighbour is not None and boid.euclidean_distance(nearest_neighbour) < 35:
        if nearest_neighbour.x - boid.x == 0.0:
            angle = math.atan((nearest_neighbour.y - boid.y) / 0.0001)
        else:
            angle = math.atan((nearest_neighbour.y - boid.y) / (nearest_neighbour.x - boid.x))

        boid.angle -= angle

def alignment(neighbours, boid):
    # move 2: orient towards the neighbours - alignment
    # calculate average angle of neighbours and move in that direction
    average_neighbours_angle = 0.0
    n_count = 0
    if neighbours:
        for neighbour_boid in neighbours:
            # fleeing birds align to fleeing birds (although currently, if
            # fleeing, avoidance overides alignment angle)
            # non-fleeing birds align to non-fleeing birds
            if (boid.status == 'fl' and neighbour_boid.status == 'fl') \
                or (boid.status != 'fl' and neighbour_boid.status != 'fl'):
                    average_neighbours_angle += neighbour_boid.angle
                    n_count+=1
        if n_count > 0:
            average_neighbours_angle /= n_count
            boid.angle = average_neighbours_angle

def cohesion(neighbours, boid):
    # move 3: move together - cohesion
    if neighbours:
        avg_x = 0.0
        avg_y = 0.0
        for neighbour_boid in neighbours:
            avg_x += neighbour_boid.x
            avg_y += neighbour_boid.y
        avg_x /= len(neighbours)
        avg_y /= len(neighbours)
        if avg_x - boid.x == 0.0:
            angle = math.atan((avg_y - boid.y) / 0.00001)
        else:
            angle = math.atan((avg_y - boid.y) / (avg_x - boid.x))
        boid.angle -= angle / 20.0
        
def predator_behaviour(canvas, list_of_boids, predator, screen_size):
    # find nearest boid
    nearest_boid = None
    shortest_distance = 999999999
    for boid in list_of_boids:
        d = boid.euclidean_distance(predator)
        if d < shortest_distance:
            shortest_distance = d
            nearest_boid = boid
        if nearest_boid.x - predator.x == 0:
            predator.angle = math.atan2(nearest_boid.y - predator.y, 0.00001)
        else:
            predator.angle = math.atan2(nearest_boid.y - predator.y, nearest_boid.x - predator.x)
    predator.flock(canvas, screen_size, predator_speed)
    canvas.after(100, predator_behaviour, canvas, list_of_boids, predator, screen_size)

def boid_behaviours(canvas, list_of_boids, predator, screen_size, t):
    t+=1
    # find neighbours
    for boid in list_of_boids:
        if boid.euclidean_distance(predator) < 1:
            # 90% chance (or whatever p_catch_prey is) that 
            # predator will catch prey if they are within 1 unit of 
            # each other. If prey is caught, print 1 on screen and exit
            if random.randrange(1, 100) < p_catch_prey:
                print('1')
                #print(t)
                window.destroy()
                return
        neighbours = []
        for b in list_of_boids:
            # if b is nearby current boid, then it is a neighbour and 
            # make sure neighbor boid is not current boid
            if boid.euclidean_distance(b) < 75 and (not boid.euclidean_distance(b) == 0):
                neighbours.append(b)
                
            # for all boids that are not currently fleeing and haven't 
            # already been alerted, check if any of their neigbors are fleeing
            if boid.alert_time is None \
                and (not boid.euclidean_distance(b) == 0) \
                and boid.euclidean_distance(b) < detection_range \
                and b.status == 'fl':
                    boid.alert_time = t
                
        nearest_neighbour = None
        # finding nearest neighbour
        if neighbours:
            shortest_distance = 999999999
            for neighbour_boid in neighbours:
                d = boid.euclidean_distance(neighbour_boid)
                if d < shortest_distance:
                    shortest_distance = d
                    nearest_neighbour = neighbour_boid

        separation(nearest_neighbour, boid)
        alignment(neighbours, boid)
        cohesion(neighbours, boid)
        
        # If a boid hasn't already been alerted and it is in detection
        # range of the predator, it becomes alerted
        if boid.alert_time is None \
            and boid.euclidean_distance(predator) < detection_range:
                boid.alert_time = t
        
        # avoidance has to be run last (after separation, alignment
        # and cohesion) because avoidance (the angle set in avoidance,
        # i.e. fleeing) supercedes all other rules/angles
        #
        # if boid hasn't begun fleeing but t > alert_time + response time:
        # set angle to avoid the predator
        if boid.alert_time is not None and t > boid.alert_time + boid.rt:
                avoidance(predator, boid, t)
                
        boid.flock(canvas, screen_size, boid_max_speed)
        
    # If no more boids on screen, print 0 and exit
    boids_on_screen = [b for b in list_of_boids if min(b.x, b.y) < screen_size and min(b.x, b.y) > 0]
    if len(boids_on_screen) == 0: 
        print('0')
        window.destroy()
        return
        
    canvas.after(100, boid_behaviours, canvas, list_of_boids, predator, screen_size, t)

t = 0
def main(no_of_boids, screen_size):
    global window
    window = tkinter.Tk()
    canvas = initialise_canvas(window, screen_size)
    list_of_boids = create_boids(canvas, no_of_boids, p_vigilant, response_time_lower, response_time_upper)
    predator = create_predator(canvas)
    boid_behaviours(canvas, list_of_boids, predator, screen_size, t)
    predator_behaviour(canvas, list_of_boids, predator, screen_size)
    window.mainloop()
    
#main(no_of_boids, screen_size)


