import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

# Carica i dati
column_names = ['x', 'y', 'z']
waypoints_data = pd.read_csv('L_traj_waypoints.csv', header=None, names=column_names)

# Estrai le coordinate x, y, z
x_points = waypoints_data['x']
y_points = waypoints_data['y']
z_points = waypoints_data['z']

# Crea il grafico 3D
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')

# # Etichette degli assi
# ax.set_xlabel('X')
# ax.set_ylabel('Y')
# ax.set_zlabel('Z')

# # Colormap
# cmap = cm.get_cmap('viridis')
# norm = plt.Normalize(0, len(x_points))
# colors = cmap(norm(range(len(x_points))))

# # Funzione di aggiornamento per l'animazione
# def update(frame):
#     ax.clear()
#     ax.set_xlabel('X')
#     ax.set_ylabel('Y')
#     ax.set_zlabel('Z')
#     for i in range(frame):
#         ax.plot(x_points[i:i+2], y_points[i:i+2], z_points[i:i+2], color=colors[i])
#     return fig,

# # Crea l'oggetto FuncAnimation
# ani = animation.FuncAnimation(fig, update, frames=len(x_points), interval=100, blit=False)




import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

def plot_colored_trajectory(csv_file):
    """
    Plotta una traiettoria 3D con i punti colorati secondo una colormap.

    Args:
    csv_file (str): Il percorso del file CSV contenente i waypoint.
    """
    # Carica i dati
    column_names = ['x', 'y', 'z']
    waypoints_data = pd.read_csv(csv_file, header=None, names=column_names)

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

    # Colormap
    cmap = plt.get_cmap('viridis')
    norm = plt.Normalize(0, len(x_points))
    colors = cmap(norm(range(len(x_points))))

    # Plot dei punti con colori
    scatter = ax.scatter(x_points, y_points, z_points, c=colors, marker='o')

    # Aggiungi la colorbar
    cbar = plt.colorbar(scatter, ax=ax)
    cbar.set_label('Frame')

    # Mostra il grafico
    plt.show()




# Mostra l'animazione
# plt.show()


# Esempio di utilizzo della funzione
plot_colored_trajectory('L_traj_waypoints.csv')