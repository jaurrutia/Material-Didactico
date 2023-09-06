
import numpy as np
import matplotlib.pyplot as plt
import paq.raices as rt

x = np.linspace(.1,2*np.pi, 30)

def func(x):
    return np.sin(2*x)
def dfunc(x):
    return 2 * np.cos(2* x)

# Visualización de nuestra función para posibles raices
plot1 = plt.figure(1)
plt.plot(x,func(x), marker = '*', label = r'$f(x)$')
plt.plot(x,np.zeros(len(x)), label = 'Eje x')
plt.legend()

intervalos = rt.root_int(func, x)
int = intervalos[0]

# Parámetros del método de Newton-Rapshon
rts = int[0]
tol = .00001
n_tot = 100
delta_list = []
delta_x = - func(rts) / dfunc(rts)
delta_list.append(delta_x)
print(delta_x)
rts += delta_x
i = 1

# Algoritmo del método Newton
while ( abs(delta_x) > tol and i < n_tot):
    delta_x = - func(rts) / dfunc(rts)
    delta_list.append(delta_x)
    print(delta_x)
    rts += delta_x
    i += 1

print("Numero de interaciones:", i)
print("La raíz está en x = ", rts)


# Visualización del error como función de los pasos
# Gráfica del error
plot2 = plt.figure(2)
plt.plot(delta_list)
plt.xscale('log')

plt.show()
