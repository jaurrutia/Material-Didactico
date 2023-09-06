
import numpy as np
import matplotlib.pyplot as plt # Un paquete de graficos
import paq.mincuad as mc   # Importar desde un subdirectorio

x = np.linspace(0, 10, 30)
error = np.random.rand(len(x)) * 10
y_exp = 3 * x + 2 + error


[m, b] = mc.minimos_cuadrados(x,y_exp)
y_teo = m * x + b

print(m, b)

s_res = y_teo - y_exp
s_res = np.dot(s_res,s_res)  # producto punto  a.a = |a|^2

s_tot = y_exp - np.mean(y_exp)
s_tot = np.dot(s_tot,s_tot)  # producto punto  a.a = |a|^2

r2 = 1 - s_res/s_tot


fig , ax = plt.subplots()

ax.errorbar(x, y_exp, yerr = error, marker = '*', label = 'Experimental')
ax.plot(x, y_teo, color = 'r', label ='Ajuste lineal')
plt.legend()
ax.set_title('m = ' + str(m) + ', b = ' + str(b) + ', r^2 = ' + str(r2))
ax.set_xlabel(r'$x$')
ax.set_ylabel(r'$y(x) = m x + b$')


plt.show()
