
import matplotlib.pyplot as plt # Un paquete de graficos
import numpy as np              # Computo Numérico.

print('''
import matplotlib.pyplot as plt # Un paquete de graficos
import numpy as np              # Computo numérico.
''')

# Creacion de arreglos
print('En NumPy podemos crear arreglos por default con los siguientes metodos:')
print("""
|   Método |             Descripción           |
|----------|-----------------------------------|
|  `array` | Crea un arreglo para la cual los elementos son proporcionados por un objeto similar a una matriz, que, por ejemplo, puede ser una lista de Python (anidada), una tupla, una secuencia iterable u otra instancia de `ndarray`|
|  `zeros` | Crea una matriz con las dimensiones y el tipo de datos especificados que se rellena con ceros|
|  `ones`  | Crea una matriz con las dimensiones y el tipo de datos especificados que se rellena con unos|
|   `diag` | Crea una matriz diagonal con valores especificados a lo largo de la diagonal y ceros en el resto|
| `arange` | Crea un arreglo con valores espaciados uniformemente entre los valores de inicio, final e incremento especificados|
|`linspace`| Crea un arreglo con valores espaciados uniformemente entre los valores iniciales y finales especificados, utilizando un número especificado de elementos|
|`logspace`| Crea un arreglo con valores espaciados logarítmicamente entre los valores iniciales y finales dados|
|`meshgrid`| Genera arreglo de coordenadas (y matrices de coordenadas de mayor dimensión) a partir de vectores de coordenadas unidimensionales|
|`fromfunction`| Crea una matriz y la llena con valores especificados por una función determinada, que se evalúa para cada combinación de índices para el tamaño de matriz dado|
|`fromfile` | Crea una matriz con los datos de un archivo binario (o de texto). NumPy también proporciona una función correspondient `np.tofile` con la que las matrices NumPy se pueden almacenar en el disco y luego leerlas usando `np.fromfile`|
|`genfromtxt,np.loadtxt`| Cree una matriz a partir de los datos leídos de un archivo de texto, por ejemplo, un archivo de valores separados por comas (CSV). La función np.genfromtxt también admite archivos de datos con valores perdidos|
|`random.rand`| Genera una  matriz con números aleatorios que se distribuyen uniformemente entre 0 y 1. También hay otros tipos de distribuciones disponibles en el np. módulo aleatorio.|
""")

input('')
print('Vamos a crear una list `x`, y una lista `y_i` con los comandos siguientes:')
x = np.linspace(0, 2*np.pi, 100) # Creamos un arreglo con número de 0 a 2 Pi con 100 valores
y_1 = np.zeros( len(x))  # Creamos un arreglo con puros ceros, con el mismo núero de elemtnos que # XXX:
y_2 = np.zeros(len(x))
y_3 = np.zeros(len(x))
print("""
x = np.linspace(0, 2*np.pi, 100)
y_1 = np.zeros( len(x))
y_2 = np.zeros(len(x))
y_3 = np.zeros(len(x))
plt.plot(x, y,marker =  ',', color = "m")
""")
plt.plot(x, y_1,marker =  ',', color = "m")

input('')
plt.show()
print('plt.show()')


input('')
print('Para modificar los valores del arreglo podemos cambiar los elementos, uno por uno con un loop:')
i = 0
while i < len(y_2):
    y_2[i] = 3 * x[i] * x[i] + 8
    i += 1
print('''i = 0
while i < len(y_2):
    y_2[i] = 3 * x[i] * x[i] + 8
    i += 1
''')
print(y_2)
input('')
plt.plot(x,y_2)
plt.show()

print('Pero una forma más inteligente sería:')
y_3 = 3 * x*x + 8
print('y_3 = 3 * x*x + 8')
input('')

print('''
plt.plot(x, y_1,marker =  ',', color = "m", label=r'$y_1(x)$')
plt.plot(x,y_2, label=r'$y_2(x)$')
plt.plot(x,y_3, marker  = '*', color = "r", label=r'$y_3(x)$')

plt.ylabel('$y_i(x)$')
plt.xlabel('$x$')
plt.legend()

plt.show()
''')

input('')
plt.plot(x, y_1,marker =  ',', color = "m", label=r'$y_1(x)$')
plt.plot(x,y_2, label=r'$y_2(x)$')
plt.plot(x,y_3, marker  = '*', color = "r", label=r'$y_3(x)$')

plt.ylabel('$y_i(x)$')
plt.xlabel('$x$')
plt.legend()

plt.show()
