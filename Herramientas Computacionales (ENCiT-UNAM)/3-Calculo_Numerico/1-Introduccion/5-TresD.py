
import numpy as np
import matplotlib.pyplot as plt # Un paquete de graficos
from mpl_toolkits.mplot3d import Axes3D

# Vamos a crear algunos datos para graficas en 3D

x = np.linspace(-np.pi, np.pi, 50)
X, Y = np.meshgrid(x,  x)  # Mesh grid nos crea una lista en NxN, donde N es la longitud de un arreglo
print("X = np.meshgrid(3 * np.linspace(-np.pi, np.pi, 50) )\n", Y)
print("Y = np.meshgrid(np.linspace(-np.pi, np.pi, 50) )\n", Y)
Z = np.cos(X*Y)


# Grafica de densidad

fig_all, ax_all = plt.subplots()  # Vamos a crear una figura queincluya todo
fig1, ax1 = plt.subplots()   # Creamos una figura y el eje coordenado ax1
fig2, ax2 = plt.subplots()   # Creamos una figura y el eje coordenado ax2


im = ax1.imshow(Z,                                  # La matrix que estamos graficando
        extent=(-np.pi, np.pi, -np.pi, np.pi)) # (-x, x, -y, y)  limits
ax1.set_title('Density Plot')
fig1.colorbar(im)

im = ax_all.imshow(Z, extent=(-np.pi, np.pi, -np.pi, np.pi))  # Nombramos esta vriable porque vamos a usar sus datos para la barra de colores
fig_all.colorbar(im, orientation='vertical', shrink=0.8)


CS = ax2.contour(X, Y, Z)                # Contour plot, también aquí guardamos los datos
ax2.clabel(CS, inline = True, fontsize = 8) # Contour labels
ax2.set_title('Contour Plot')

CS = ax_all.contour(X, Y , Z,  colors='k')
ax_all.clabel(CS,  fontsize = 8)
ax_all.set_title('Density & Contour Plot')


fig3D = plt.figure()
ax3D = Axes3D(fig3D)
ax3D.plot_surface(X, Y, Z, rstride=1, cstride=1)

plt.show()  # Como creamos tres figuras, nos mostrara las tres
