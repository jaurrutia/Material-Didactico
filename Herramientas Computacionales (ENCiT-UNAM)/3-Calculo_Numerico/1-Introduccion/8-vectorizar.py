
import numpy as np
import matplotlib.pyplot as plt # Un paquete de graficos

def escalon(x, x0):
    return 1 if x > x0 else 0

escalon = np.vectorize(escalon)

x = np.linspace(-1, 1, 50) * np.pi
y = np.sin(x)
z = y * escalon(x,0)
zz = y * escalon(x, np.pi/2.)

fig , ax = plt.subplots()

ax.plot(x, y, color = 'r', label =r'$\sin(x)$', marker = '*')
ax.plot(x, z, color = 'g', label =r'$\sin(x)*\Theta(x)$', marker = '*')
ax.plot(x, zz, color = 'b', label =r'$\sin(x)*\Theta(x-\pi/2)$', marker = '*')

plt.legend()
ax.set_xlabel(r'$x$')
ax.set_ylabel(r'$y(x)$')


plt.show()
