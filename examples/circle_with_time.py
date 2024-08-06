import numpy as np

numRobots = 1

r = 0.3
height = 0.5
w = 2 * np.pi / numRobots
T = 2 * 2 * np.pi / w

# horizontal circles
# for i in range(0, numRobots):
#     phase = 2 * np.pi / numRobots * i

#     with open("timed_waypoints_circle{}.csv".format(i), "w") as f:
#         f.write("t,x,y,z,yaw\n")

#         for t in np.linspace(0, T, 100):
#             f.write("{},{},{},{},{}\n".format(
#                 t, r * np.cos(w * t + phase), r * np.sin(w * t + phase), height, 0))



def generate_horizontal_circles(numRobots=1, r=0.3, height=0.3, numPoints=100, output_file="timed_waypoints_circle"):
    """
    Genera file CSV con waypoints per cerchi orizzontali per un numero specificato di robot.

    Parametri:
    numRobots (int): Numero di robot per cui generare i waypoints.
    r (float): Raggio dei cerchi.
    height (float): Altezza fissa dei cerchi dal suolo.
    numPoints (int): Numero di punti per cerchio.
    """
    w = 2 * np.pi / numRobots
    T = 2 * 2 * np.pi / w

    # Cerchi orizzontali
    for i in range(numRobots):
        phase = 2 * np.pi / numRobots * i

        with open(output_file+"_"+str(i)+".csv", "w") as f:
            f.write("t,x,y,z,yaw\n")

        for t in np.linspace(0, T, numPoints):
            f.write("{},{},{},{},{}\n".format(
                t, r * np.cos(w * t + phase), r * np.sin(w * t + phase), height, 0))


