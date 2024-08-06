import os

import numpy as np


def generate_horizontal_circles(numRobots=1, r=0.3, height=0.5, numPoints=1000, output_file="timed_waypoints_circle"):
    """
    Genera file CSV con waypoints per cerchi orizzontali per un numero specificato di robot.

    Parametri:
    numRobots (int): Numero di robot per cui generare i waypoints.
    r (float): Raggio dei cerchi.
    height (float): Altezza fissa dei cerchi dal suolo.
    numPoints (int): Numero di punti per cerchio.
    """
    duration = 10
    w = 2 * np.pi / numRobots
    T = 2 * 2 * np.pi / w
    # T = duration

    # Cerchi orizzontali
    for i in range(numRobots):
        phase = 2 * np.pi / numRobots * i

        with open(output_file+"_"+str(i)+".csv", "w") as f:
            # f.write("t,x,y,z\n")

            for t in np.linspace(0, T, numPoints):
                f.write("{},{},{}\n".format(
                    r * np.cos(w * t + phase), r * np.sin(w * t + phase), height))

    # returning the absolute file path not the relative one
    return os.path.abspath(output_file+"_0.csv")



def generate_horizontal_circles_with_starting_point(numRobots=1, r=0.3, height=0.3, numPoints=100, output_file="timed_waypoints_circle_starting_point", start_point=(0, 0)):
    """
    Genera file CSV con waypoints per cerchi orizzontali per un numero specificato di robot.

    Parametri:
    numRobots (int): Numero di robot per cui generare i waypoints.
    r (float): Raggio dei cerchi.
    height (float): Altezza fissa dei cerchi dal suolo.
    numPoints (int): Numero di punti per cerchio.
    start_point (tuple): Punto di partenza (x, y) del robot.
    """
    w = 2 * np.pi / numRobots
    T = 2 * np.pi / w  # Periodo del cerchio

    for i in range(numRobots):
        phase = 2 * np.pi / numRobots * i

        with open(output_file+"_"+str(i)+".csv", "w") as f:
            # Traiettoria dal punto di partenza alla circonferenza
            for t in np.linspace(0, 1, 10):
                x = start_point[0] + (r * np.cos(phase) - start_point[0]) * t
                y = start_point[1] + (r * np.sin(phase) - start_point[1]) * t
                f.write("{},{},{}\n".format(x, y, height))

            # Traiettoria sulla circonferenza
            for t in np.linspace(0, T, numPoints - 20):
                x = r * np.cos(w * t + phase)
                y = r * np.sin(w * t + phase)
                if t > 0:  # Evita di riscrivere il primo punto della circonferenza, che è lo stesso della fine del ciclo precedente
                    f.write("{},{},{}\n".format(x, y, height))

            # Torna al punto di partenza partendo dal punto finale della circonferenza
            for t in np.linspace(0, 1, 10):
                x = r * np.cos(w * T + phase) + (start_point[0] - r * np.cos(w * T + phase)) * t
                y = r * np.sin(w * T + phase) + (start_point[1] - r * np.sin(w * T + phase)) * t
                if t > 0:  # Evita di riscrivere il primo punto della circonferenza, che è lo stesso della fine del ciclo precedente
                    f.write("{},{},{}\n".format(x, y, height))

    return os.path.abspath(output_file+"_0.csv")
