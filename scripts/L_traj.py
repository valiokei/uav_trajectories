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

    
    # si è notato che il crazyflie a gestire meglio la traiettoria generata a partire da questo tipo di waypoints almeno in linea retta come in questo caso

    waypoints.append([x_start, y_start, height])
    waypoints.append([x_start, y_start - distance, height])
    waypoints.append([x_start, y_start, height])



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
