
import matplotlib.pyplot as plt # Un paquete de graficos
import numpy as np              # Computo Numérico.


x = np.arange(0, 2*np.pi, .1) # Creamos un arreglo con número de 0 a 2 Pi con 100 valores
y = np.sin(x)
x_1 = x[:-1]
y_1 = -1 * np.sin(x_1)


fig , axs = plt.subplots()
axs.plot(x,y, color = 'g', label = r'$\sin(x)$')
axs.plot(x_1,y_1, color = 'r', label = r'$-\sin(x)$')

axs.set_title('Seno y menos seno de x')
axs.axis('equal')
#plt.set(xlim=(-3, 3), ylim=(-3, 3))
axs.set_ylabel(r'$y_i(x)$')
axs.set_xlabel(r'$x $')
axs.grid()
plt.legend()

plt.show()
