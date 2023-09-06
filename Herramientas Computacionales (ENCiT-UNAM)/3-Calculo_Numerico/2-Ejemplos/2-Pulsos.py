
import numpy as np
import matplotlib.pyplot as plt # Un paquete de graficos
import csv


def pulse(x, position, height, width):
    # x es un np.array
    return height * (x > (position - width/2)) * (x <= (position + width/2))

a = np.array([1, 2, 3, 4])
b = np.array([4, 3, 2, 1])
print('''
a = np.array([1, 2, 3, 4])
b = np.array([4, 3, 2, 1])
a < b -->''', a<b)
print("1 * (a < b) ---> ", 1*(a<b))

print("Equivalente a un `and`: print(np.all(a < b) ---> ",  np.all(a < b))
print("Equivalente a un `or`: print(np.any(a < b) ---> ",  np.any(a < b))

#input('')
print('Empleemos esto para definir a un pulso:')
print('''def pulse(x, position, height, width):
    return height * (x >= position) * (x <= (position + width))
''')

x = np.linspace(-11,10,100)
x0 = -2
h = 5
p = pulse(x, x0, h, 1/h )

fig, ax = plt.subplots()
ax.plot(x,p , label = r'$h = '+str(h)+'$')
ax.set_xlabel('x')
ax.set_ylabel('Pulso')

plt.legend()
plt.show()

fig, ax = plt.subplots()
ax.plot(x,p , label = r'$h = '+str(h)+'$')
h = 2
p = pulse(x, x0, h, 1/h )
ax.plot(x,p , label = r'$h = '+str(h)+'$')
ax.set_xlabel('x')
ax.set_ylabel('Pulso')

plt.legend()
plt.show()


fig, ax = plt.subplots()
h_list = np.array(range(1,21,2))
lista = np.zeros((len(h_list), len(x)+1))
for i in range(0,len(h_list)-1):
    h = h_list[i]
    p = pulse(x, x0, h, 1/h )
    ax.plot(x,p , label = r'$h = '+str(h)+'$')

#    lista[i,0] = h
#    lista[i,0:] = p
#writer.writerow([h].append(p)

#with open('pulsos.csv', 'w', newline='') as csvfile:  # La w significa de write
#    writer = csv.writer(csvfile)

print(h_list)
ax.set_xlabel('x')
ax.set_ylabel('Pulso')
plt.legend()
plt.show()
