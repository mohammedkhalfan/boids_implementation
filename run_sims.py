# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 19:17:45 2022

@author: mk5636
"""
import run_boids
import pandas as pd


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

# change the n here
n = 100

# =============================================================================
# ##generate different  data acceleration_param-----------------------------
# list_acceleration_param = []
# p_acceleration_param = [10, 15, 20, 25, 30]
# 
# for v in p_acceleration_param:
#     print("acceleration_param: ", v)
#     run_boids.acceleration_param = v
#     for x in range(n):
#         run_boids.main(no_of_boids, screen_size)
#     list_acceleration_param.append(run_boids.list_result)
#     run_boids.list_result =[]
#     print(list_acceleration_param)
# 
# ## save it to a csv, and rename the columns.
# p_acceleration_param_pd=pd.DataFrame(data=list_acceleration_param).T
# p_acceleration_param_pd.columns = p_acceleration_param
# p_acceleration_param_pd.to_csv('D:/acceleration_param_time.csv')
# 
# # set to config value
# run_boids.acceleration_param = 20
# 
# =============================================================================



## This is how you iterate 10 (n) times on
## different values for p_vigilant
## (n times on each value of p_vigilant)
## (in this example with n = 10 and 5 values
## for p_vigilance, total iterations = 50)
## n: number of iterations
## p_vigilant_values: list of values for p_vigilance

# =============================================================================
# ##generate different  data predator_speed
# list_predator_speed= []
# p_predator_speed = [2.6, 2.8, 3, 3.2, 3.4]
# 
# for v in p_predator_speed:
#     print("predator_speed: ", v)
#     run_boids.predator_speed = v
#     for x in range(n):
#         run_boids.main(no_of_boids, screen_size)
#     list_predator_speed.append(run_boids.list_result)
#     run_boids.list_result =[]
#     print(list_predator_speed)
# 
# ## save it to a csv, and rename the columns.
# p_predator_speed_pd=pd.DataFrame(data=list_predator_speed).T
# p_predator_speed_pd.columns = p_predator_speed
# # where to save file
# p_predator_speed_pd.to_csv('D:/predator_speed_time.csv')
# # set to config value
# run_boids.predator_speed = 3
# =============================================================================


# =============================================================================
# ##generate different  data boid_max_speed
# list_boid_max_speed= []
# p_boid_max_speed = [2.6, 2.8, 3, 3.2, 3.4]
# 
# for v in p_boid_max_speed :
#     print("boid_max_speed : ", v)
#     run_boids.boid_max_speed  = v
#     for x in range(n):
#         run_boids.main(no_of_boids, screen_size)
#     list_boid_max_speed.append(run_boids.list_result)
#     run_boids.list_result =[]
#     print(list_boid_max_speed)
# 
# ## save it to a csv, and rename the columns.
# p_predator_speed_pd=pd.DataFrame(data=list_boid_max_speed).T
# p_predator_speed_pd.columns = p_boid_max_speed 
# # where to save file
# p_predator_speed_pd.to_csv('D:/boid_max_speed_time.csv')
# # set to config value
# run_boids.boid_max_speed  = 3
# 
# =============================================================================











##generate different  data detection_range-----------------------------
list_detection_range = []
p_detection_range = [50, 75, 100, 125, 150]

for v in p_detection_range:
    print("detection_range: ", v)
    run_boids.detection_range = v
    for x in range(n):
        run_boids.main(no_of_boids, screen_size)
    list_detection_range.append(run_boids.list_result)
    run_boids.list_result =[]
    print(list_detection_range)

## save it to a csv, and rename the columns.
p_detection_range_pd=pd.DataFrame(data=list_detection_range).T
p_detection_range_pd.columns = p_detection_range
p_detection_range_pd.to_csv('D:/detection_range_time.csv')

# set to config value
run_boids.detection_range = 100

##generate different  data no_of_boids-----------------------------------
list_no_of_boids= []
p_no_of_boids = [10, 20, 30, 40, 50]

for v in p_no_of_boids:
    print("no_of_boids: ", v)
    run_boids.no_of_boids = v
    for x in range(n):
        run_boids.main(v, screen_size)
    list_no_of_boids.append(run_boids.list_result)
    run_boids.list_result =[]
    print(list_no_of_boids)

## save it to a csv, and rename the columns.
p_no_of_boids_pd=pd.DataFrame(data=list_no_of_boids).T
p_no_of_boids_pd.columns = p_no_of_boids
# where to save file
p_no_of_boids_pd.to_csv('D:/no_of_boids_time.csv')
# set to config value
no_of_boids = 40






##generate different vigilant_values data------------------------------

list_p_vigilant = []
p_vigilant_values = [10, 20, 30, 40, 50]

for v in p_vigilant_values:
    print("PERCENT VIGILANCE: ", v)
    run_boids.p_vigilant = v
    for x in range(n):
        run_boids.main(no_of_boids, screen_size)
    list_p_vigilant.append(run_boids.list_result)
    run_boids.list_result =[]
    print(list_p_vigilant)

## save it to a csv, and rename the columns.
p_vigilant_pd=pd.DataFrame(data=list_p_vigilant).T
p_vigilant_pd.columns = p_vigilant_values
p_vigilant_pd.to_csv('D:/vigilant_time.csv')
# set to config value
run_boids.p_vigilant = 20



##generate different response_time-----------------------------------
list_response_time = []
list_response_time_lower= [5, 8, 11, 14, 17]
list_response_time_upper = [15, 20, 25, 30,35]
list_response_time_columns = ['5+15','8+20', '11+25', '14+30', '17+35']
i_response_time = 0

while i_response_time < 5: 
    run_boids.response_time_lower = list_response_time_lower[i_response_time]
    run_boids.response_time_upper = list_response_time_upper[i_response_time]
    print("response time: lower:",list_response_time_lower[i_response_time],
           ", upper:",list_response_time_upper[i_response_time])
    for x in range(n):
        run_boids.main(no_of_boids, screen_size)
    list_response_time.append(run_boids.list_result)
    run_boids.list_result =[]
    print(list_response_time)
    i_response_time = i_response_time + 1
    
## save it to a csv, and rename the columns.
p_response_time=pd.DataFrame(data=list_response_time).T
p_response_time.columns = list_response_time_columns
p_response_time.to_csv('D:/response_time.csv')
# set to config value
run_boids.response_time_lower = 11
run_boids.response_time_upper = 25










