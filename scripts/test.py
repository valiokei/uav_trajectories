#!/usr/bin/env python

import argparse
# set file path as working python folder
import os
import sys

import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.express as px
from circle_with_time import generate_horizontal_circles_with_starting_point
from square_trajectory import generate_square_trajectory
from generate_trajectory import process_trajectory
from matplotlib import animation
from mpl_toolkits.mplot3d import Axes3D
from plot_trajectory import plot_trajectory_from_csv
from line_traj import generate_line_trajectory
from L_traj import generate_L_trajectory

# import scipy.interpolate


# horizontal circles
# trajname = 'circle'
# outputFilePath = generate_horizontal_circles_with_starting_point(
#     numRobots=1, r=0.3, height=0.3, numPoints=50,start_point=(0, 0),output_file=trajname)

# trajname = 'square'
# outputFilePath = generate_square_trajectory(start_point=(0, 0), side_length=0.4, height=0.25, num_points_per_side=6, output_file=trajname) 

# trajname = 'line'
# outputFilePath = generate_line_trajectory(start_point=[0, 0, 0], length=0.3, num_points=10, num_repetitions=3, axis=0, output_file=trajname+"_waypoints")

trajname = 'L_traj'
outputFilePath = generate_L_trajectory( start_point=(0, 0, 0.3), height=0.3, distance=0.75, num_points=20, output_file=trajname+"_waypoints")


# execute a command in the shell
os.system(
    './genTrajectory -i '+outputFilePath+' --v_max 0.5 --a_max 0.5 -o '+trajname+'.csv')


data = pd.read_csv(
    '/home/valiokei/Documenti/GitHub/uav_trajectories/'+trajname+'.csv', header=None, names=['x', 'y', 'z'])


# column_names = ['x', 'y', 'z']
# waypoints_data = pd.read_csv('timed_waypoints_circle_starting_point_0.csv', header=None, names=column_names)

# # Estrai le coordinate x, y, z
# x_points = waypoints_data['x']
# y_points = waypoints_data['y']
# z_points = waypoints_data['z']

# # Crea il grafico 3D
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')

# # Etichette degli assi
# ax.set_xlabel('X')
# ax.set_ylabel('Y')
# ax.set_zlabel('Z')

# # Funzione di aggiornamento per l'animazione
# def update(frame):
#     ax.clear()
#     ax.set_xlabel('X')
#     ax.set_ylabel('Y')
#     ax.set_zlabel('Z')
#     ax.plot(x_points[:frame], y_points[:frame], z_points[:frame], marker='o')
#     return fig,

# # Crea l'oggetto FuncAnimation
# ani = animation.FuncAnimation(fig, update, frames=len(x_points), interval=100, blit=False)

# # Mostra l'animazione
# plt.show()


# Plot the trajectory
plot_trajectory_from_csv(trajname+".csv")
