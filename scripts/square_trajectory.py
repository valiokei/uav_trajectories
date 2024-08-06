import numpy as np
import os

def generate_square_trajectory(start_point, side_length, height, num_points_per_side, output_file):

    
    waypoints = []

    start_point = [start_point[0], start_point[1], height]

    corners = [
        [start_point[0] + side_length/2, start_point[1]+ side_length/2, height],
        [start_point[0] + side_length/2, start_point[1] - side_length/2, height],
        [start_point[0]- side_length/2, start_point[1] - side_length/2, height],
        [start_point[0]- side_length/2, start_point[1]+ side_length/2, height]
    ]


    firstPointOfTheTrajectory = [start_point[0] + side_length/2, start_point[1], height]

    #from start point to the first point  using linespace
    x = np.linspace(start_point[0], firstPointOfTheTrajectory[0], 5)
    y = np.linspace(start_point[1], firstPointOfTheTrajectory[1], 5)
    z = np.linspace(start_point[2], firstPointOfTheTrajectory[2], 5)

    for i in range(5):
        waypoints.append([x[i], y[i], z[i]])


    #from first point to the second point using linespace
    x = np.linspace(firstPointOfTheTrajectory[0], corners[1][0], int(num_points_per_side/2))
    y = np.linspace(firstPointOfTheTrajectory[1], corners[1][1], int(num_points_per_side/2))
    z = np.linspace(firstPointOfTheTrajectory[2], corners[1][2], int(num_points_per_side/2))

    for i in range(num_points_per_side//2):
        waypoints.append([x[i], y[i], z[i]])
    
    #from first corner to the second corner using linespace
    x = np.linspace(corners[1][0], corners[2][0], num_points_per_side)
    y = np.linspace(corners[1][1], corners[2][1], num_points_per_side)
    z = np.linspace(corners[1][2], corners[2][2], num_points_per_side)

    for i in range(num_points_per_side):
        waypoints.append([x[i], y[i], z[i]])
    
    #from second corner to the third corner using linespace
    x = np.linspace(corners[2][0], corners[3][0], num_points_per_side)
    y = np.linspace(corners[2][1], corners[3][1], num_points_per_side)
    z = np.linspace(corners[2][2], corners[3][2], num_points_per_side)

    for i in range(num_points_per_side):
        waypoints.append([x[i], y[i], z[i]])
    

    #from second corner to the third corner using linespace
    x = np.linspace(corners[3][0], corners[0][0], num_points_per_side)
    y = np.linspace(corners[3][1], corners[0][1], num_points_per_side)
    z = np.linspace(corners[3][2], corners[0][2], num_points_per_side)

    for i in range(num_points_per_side):
        waypoints.append([x[i], y[i], z[i]])

    #from third corner to the fourth corner using linespace
    x = np.linspace(corners[0][0], firstPointOfTheTrajectory[0], int(num_points_per_side/2))
    y = np.linspace(corners[0][1], firstPointOfTheTrajectory[1], int(num_points_per_side/2))
    z = np.linspace(corners[0][2], firstPointOfTheTrajectory[2], int(num_points_per_side/2))

    for i in range(int(num_points_per_side/2)):
        waypoints.append([x[i], y[i],z[i]])

    # from firstpoint to the starting point using linespace
    x = np.linspace(firstPointOfTheTrajectory[0], start_point[0], 5)
    y = np.linspace(firstPointOfTheTrajectory[1], start_point[1], 5)
    z = np.linspace(firstPointOfTheTrajectory[2], start_point[2], 5)

    for i in range(5):
        waypoints.append([x[i], y[i], z[i]])

    # eliminare i waypoint duplicati in sequenza
    waypoints = [waypoints[i] for i in range(len(waypoints)) if i == 0 or waypoints[i] != waypoints[i-1]]

    # Salva i waypoint in un file CSV
    with open(output_file + "_0.csv", 'w') as f:
        for waypoint in waypoints:
            f.write("{},{},{}\n".format(waypoint[0], waypoint[1], waypoint[2]))

    return os.path.abspath(output_file + "_0.csv")



# # scrivi del codice per plottare tutti i punti di passaggio significativi (starting, firstpoint, corners) e la traiettoria

# import pandas as pd
# import matplotlib.pyplot as plt 
# import matplotlib.animation as animation
# def plot_trajectory_from_csv(file_path):
#     # Carica i dati
#     column_names = ['x', 'y', 'z']
#     waypoints_data = pd.read_csv(file_path, header=None, names=column_names)

#     # Estrai le coordinate x, y, z
#     x_points = waypoints_data['x']
#     y_points = waypoints_data['y']
#     z_points = waypoints_data['z']

#     # Crea il grafico 3D
#     fig = plt.figure()
#     ax = fig.add_subplot(111, projection='3d')

#     # Etichette degli assi
#     ax.set_xlabel('X')
#     ax.set_ylabel('Y')
#     ax.set_zlabel('Z')

#     # add the waypoints
#     ax.plot(x_points, y_points, z_points, marker='o')

#     start_point = [x_points[0], y_points[0], z_points[0]]
#     height = start_point[2]
#     side_length = 0.3
#     firstPointOfTheTrajectory = [start_point[0] + side_length/2, start_point[1], height]
#      # add the starting point
#     ax.scatter(start_point[0], start_point[1], start_point[2], color='g', marker='o')

#     # add the first point of the traj
#     ax.scatter(firstPointOfTheTrajectory[0], firstPointOfTheTrajectory[1], firstPointOfTheTrajectory[2], color='r', marker='o')

#     # add the corners
#     corners = [
#         [start_point[0] + side_length/2, start_point[1]+ side_length/2, height],
#         [start_point[0] + side_length/2, start_point[1] - side_length/2, height],
#         [start_point[0]- side_length/2, start_point[1] - side_length/2, height],
#         [start_point[0]- side_length/2, start_point[1]+ side_length/2, height]
#     ]

#     for corner in corners:
#         ax.scatter(corner[0], corner[1], corner[2], color='b', marker='o')

    

#     # Mostra l'animazione
#     plt.show()

# outputFilePath = generate_square_trajectory(start_point=(0, 0), side_length=0.3, height=0.3, num_points_per_side=10, output_file="timed_waypoints_circle_starting_point")
# plot_trajectory_from_csv(outputFilePath)








