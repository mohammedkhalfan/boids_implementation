# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 19:17:45 2022

@author: mk5636
"""
import run_boids

no_of_boids = 40
run_boids.predator_speed = 3
run_boids.detection_range = 100
run_boids.p_vigilant = 20
run_boids.response_time_lower = 11
run_boids.response_time_upper = 25
run_boids.boid_max_speed = 3
run_boids.acceleration_param = 20
run_boids.p_catch_prey = 90
screen_size = 400



## This is how you iterate 10 (n) times on
## different values for p_vigilant
## (n times on each value of p_vigilant)
## (in this example with n = 10 and 5 values
## for p_vigilance, total iterations = 50)
## n: number of iterations
## p_vigilant_values: list of values for p_vigilance
n = 10
p_vigilant_values = [10, 20, 30, 40, 50]

for v in p_vigilant_values:
    print("PERCENT VIGILANCE: ", v)
    run_boids.p_vigilant = v
    for x in range(n):
        run_boids.main(no_of_boids, screen_size)
    



