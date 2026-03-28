import numpy as np
import matplotlib.pyplot as plt

# Positions du mobile
x = np.array([])

y = np.array([])  #


N = len(x)
dt = 0.04

# Calcul des vitesses
vx = (x[1:]-x[:-1]) / dt
vy = (y[1:]-y[:-1]) / dt

# Tracé des points
plt.plot(x, y, "bo")

# Tracé des vecteurs vitesse (on utilise x[:-1] car vx a N-1 valeurs)
plt.quiver(x[:-1], y[:-1],vx,vy,
angles="xy",scale_units="xy",scale=40,color="red")

# Configuration du graphique
plt.xlabel("x(m)")
plt.ylabel("y(m)")
plt.title("Chronophotographie du mouvement")
plt.axis("equal")
plt.grid()

plt.show()
