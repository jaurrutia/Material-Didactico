
import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(0,2*np.pi, 50)
y = np.sin(2*x)-np.cos(x)

plt.plot(x,y, marker = '*', label = r'$f(x)$')
plt.plot(x,np.zeros(len(x)), label = 'Eje x')

#sign = np.zeros(len(y)-1)
#for i in range(0, len(sign)):
#    sign[i] = y[i]*y[i+1]/np.abs(y[i]*y[i+1])

sign = np.zeros(len(y)-1)
intervalos = []
for i in range(0, len(sign)):
    sign[i] = y[i]*y[i+1]
    if sign[i] <= 0:
        intervalos.append([x[i], x[i+1]])
print(intervalos)

plt.plot(x[1:],sign, label = 'signo', marker = '.')

plt.legend()
plt.show()
