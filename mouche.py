import numpy as np
import matplotlib.pyplot as plt

# Coordonnées initiales de la mouche
mx = 0
my = 0

# Nombre d'itérations et liste des coordonnées
nb_iter= 100
xc = [mx]
yc = [my]

# Simulation de la trajectoire de la mouche
for _ in range(nb_iter):
    # Mettre à jour les coordonnées de manière aléatoire
    mx += np.random.randint(-5, 6)
    my += np.random.randint(-5, 6)
    xc.append(mx)
    yc.append(my)

# Affichage du graphe de la trajectoire
plt.plot(xc, yc, '-o')
plt.xlabel('X axis ')
plt.ylabel('Y axis ')
plt.title('Fly trajectory')
plt.grid(True)

# Marquer le point de départ
plt.plot(xc[0], yc[0], 'ro')
plt.text(xc[0], yc[0], 'Start', color='red', ha='right')

# Marquer le point de fin
plt.plot(xc[-1], yc[-1], 'ro')
plt.text(xc[-1], yc[-1], 'Finish', color='red', ha='left')

plt.show()
