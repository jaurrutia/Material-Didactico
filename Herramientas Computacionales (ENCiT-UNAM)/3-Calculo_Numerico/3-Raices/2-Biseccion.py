
import numpy as np
import matplotlib.pyplot as plt
import paq.raices as rt

x = np.linspace(0,2*np.pi, 50)

def func(x):
    return np.sin(2*x)-np.cos(x)

# Visualización de nuestra función para posibles raices
plt.plot(x,func(x), marker = '*', label = r'$f(x)$')
plt.plot(x,np.zeros(len(x)), label = 'Eje x')
plt.legend()
plt.show()

intervalos = rt.root_int(func, x)
int = intervalos[0]

# Parámetros del método de bisección
i = 0
n_tot = 100
tol = .000000001
a = int[0]
b = int[1]
delta_x = (b-a)
c = a + delta_x/2
delta_list = []

# Algoritmo del método de bisecciómn

while (delta_x/2 > tol and i < n_tot):
    if func(a)*func(c) > 0:
        a = c
    elif func(c)*func(b) > 0:
        b = c
    elif func(c) == 0:
        break
    i += 1
    delta_x = b-a
    delta_list.append(delta_x)
    c = a + delta_x/2
    print(delta_x)

print("Numero de interaciones:", i)
print("La raíz está en x = ", c)


# Visualización del error como función de los pasos
delta_list = np.array(delta_list)
equis = np.linspace(0,len(delta_list),20)
# Gráfica del error
plt.plot(delta_list)
# Gráfica del estimado teórico del error
plt.plot((int[1]-int[0])*2**(-equis))
plt.yscale('log')

plt.show()
