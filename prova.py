import pandas as pd

# # Load the CSV file
# file_path = 'traj1.csv'
# trajectory_data = pd.read_csv(file_path)

# # Display the first few rows of the dataframe to understand its structure
# trajectory_data.head()


# import numpy as np
# import matplotlib.pyplot as plt

# # Function to evaluate a polynomial at a given time t
# def evaluate_polynomial(coeffs, t):
#     return sum(c * t**i for i, c in enumerate(coeffs))

# # Extract segments and coefficients
# duration = trajectory_data['Duration']
# x_coeffs = trajectory_data[[f'x^{i}' for i in range(8)]].values
# y_coeffs = trajectory_data[[f'y^{i}' for i in range(8)]].values
# z_coeffs = trajectory_data[[f'z^{i}' for i in range(8)]].values

# # Initialize lists to store the trajectory points
# x_points, y_points, z_points = [], [], []

# # Evaluate the trajectory at multiple points within each segment
# num_points_per_segment = 100
# for i, dur in enumerate(duration):
#     t_vals = np.linspace(0, dur, num_points_per_segment)
#     x_points.extend(evaluate_polynomial(x_coeffs[i], t) for t in t_vals)
#     y_points.extend(evaluate_polynomial(y_coeffs[i], t) for t in t_vals)
#     z_points.extend(evaluate_polynomial(z_coeffs[i], t) for t in t_vals)


# import matplotlib.animation as animation

# # Set up the figure and the 3D axis
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# ax.set_xlim(min(x_points), max(x_points))
# ax.set_ylim(min(y_points), max(y_points))
# ax.set_zlim(min(z_points), max(z_points))
# ax.set_xlabel('X')
# ax.set_ylabel('Y')
# ax.set_zlabel('Z')
# ax.set_title('Drone Trajectory Animation')

# # Line object to update
# line, = ax.plot([], [], [], label='Drone Trajectory')

# # Initialization function for the animation
# def init():
#     line.set_data([], [])
#     line.set_3d_properties([])
#     return line,

# # Update function for the animation
# def update(num, x_points, y_points, z_points, line):
#     line.set_data(x_points[:num], y_points[:num])
#     line.set_3d_properties(z_points[:num])
#     return line,

# # Create the animation
# ani = animation.FuncAnimation(
#     fig, update, frames=len(x_points), fargs=(x_points, y_points, z_points, line), 
#     init_func=init, blit=False, interval=10, repeat=False
# )

# # Display the animation
# plt.legend()


import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D






# Carica i dati
column_names = ['x', 'y', 'z']
waypoints_data = pd.read_csv('L_traj_waypoints.csv', header=None, names=column_names)

# Estrai le coordinate x, y, z
x_points = waypoints_data['x']
y_points = waypoints_data['y']
z_points = waypoints_data['z']

# Crea il grafico 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Etichette degli assi
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Funzione di aggiornamento per l'animazione
def update(frame):
    ax.clear()
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.plot(x_points[:frame], y_points[:frame], z_points[:frame], marker='o')
    return fig,

# Crea l'oggetto FuncAnimation
ani = animation.FuncAnimation(fig, update, frames=len(x_points), interval=100, blit=False)

# Mostra l'animazione
plt.show()
