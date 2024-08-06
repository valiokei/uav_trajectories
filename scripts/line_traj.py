import numpy as np
import os

def generate_line_trajectory(start_point, length, num_points, num_repetitions, axis, output_file):
    waypoints = []
    direction = 1  # 1 significa avanti, -1 significa indietro
    
    for rep in range(num_repetitions):
        for i in range(num_points):
            current_position = start_point.copy()
            current_position[axis] += direction * (length / (num_points - 1)) * i
            waypoints.append(current_position)
        
        direction *= -1  # Inverti la direzione per il viaggio indietro
    

    # ritorna allo start point
    waypoints.append(start_point.copy())

    # Salva i waypoint in un file CSV
    with open(output_file + ".csv", 'w') as f:
        for waypoint in waypoints:
            f.write("{},{},{}\n".format(waypoint[0], waypoint[1], waypoint[2]))
    
    return os.path.abspath(output_file + ".csv")

# # Esempio di utilizzo
# start_point = [0, 0, 0]
# length = 10
# num_points = 5
# num_repetitions = 3
# axis = 0  # 0 per l'asse x, 1 per l'asse y, 2 per l'asse z
# output_file = "line_trajectory"
# csv_path = generate_line_trajectory(start_point, length, num_points, num_repetitions, axis, output_file)
# print(f"Il file CSV è stato salvato in: {csv_path}")
