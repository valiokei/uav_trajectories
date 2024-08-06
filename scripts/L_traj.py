import numpy as np
import os

def generate_L_trajectory(start_point, height, distance, num_points, output_file):
    """
    Genera una traiettoria per un drone e la salva in un file CSV.
    
    Args:
    start_point (tuple): Coordinate iniziali del drone (x, y, z).
    height (float): Altezza a cui deve salire il drone.
    distance (float): Distanza che il drone deve percorrere lungo l'asse x.
    num_points (int): Numero di punti nella traiettoria per ciascun segmento.
    output_file (str): Nome del file CSV di output senza estensione.
    
    Returns:
    str: Percorso assoluto del file CSV salvato.
    """
    waypoints = []
    
    # Coordinate iniziali
    x_start, y_start, z_start = start_point

    
    # Generazione del segmento di movimento orizzontale
    for i in range(1, num_points):
        x = x_start 
        y = y_start- distance * i / (num_points - 1)
        z = height
        waypoints.append([x, y, z])
    
    # Generazione del segmento di ritorno orizzontale
    for i in range(1, num_points):
        x = x_start 
        y = y_start - distance - distance * i / (num_points - 1)
        z = height
        waypoints.append([x, y, z])
    

    
    # ritorna allo start point
    # waypoints.append([x_start, y_start, z_start])

    # Salva i waypoint in un file CSV
    with open(output_file + ".csv", 'w') as f:
        for waypoint in waypoints:
            f.write("{},{},{}\n".format(waypoint[0], waypoint[1], waypoint[2]))
    
    return os.path.abspath(output_file + ".csv")

# # Esempio di utilizzo
# start_point = [0, 0, 0]
# height = 10
# distance = 20
# num_points = 10
# output_file = "drone_trajectory"
# csv_path = generate_trajectory(start_point, height, distance, num_points, output_file)
# print(f"Il file CSV è stato salvato in: {csv_path}")
