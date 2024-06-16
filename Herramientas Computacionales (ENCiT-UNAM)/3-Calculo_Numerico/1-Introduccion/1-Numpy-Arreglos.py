

import numpy as np

print("""Empleando la librerio numpy, importándola como

\t import numpy as np

podemos acceder a funciones como:
""")

print("np.sin( np.pi ) = ", np.sin(np.pi))

# Una de las principales herramientas de numpy es la estructuración de datos en un arreglo ordenado,
# lo que comúnmente se concoe como MATRICES. Para esto se emplea el iterable denominado LISTA y modifica
# sus propiedades mediante la clase de narray.
# Recordemos, primero, cómo operan las listas

list_1 = [1, 2, 3]
list_2 = [4, 5, 6]

print("Las listas en Python, por default, tienen la siguiente álgebra:")
print("list_1 = ", list_1)
print("list_2 = ", list_2)

print("\nlist_1 + list_2 = ", list_1 + list_2)
print("list_1 * 5 =  ", list_1 *5)

input('')
# Ahora, empleemos arreglos:

print("\nEmpleemos la siguiente función de numpy: array()\n")

array_1 = np.array(list_1)
array_2 = np.array(list_2)
print("array_1 = np.array(list_1)  -->  ", array_1)
print("array_2 = np.array(list_2)  -->  ", array_2)

print("\narray_1 + array_2 = ", array_1 + array_2)
print("array_1 * 5 =  ", array_1 *5)

# Veamos cómo podemos hacer más general a los arreglos, anidando listas
print("\nAnalicemos más propiedades de loa arreglos con el siguiente ejemplo:\n ")
input('')

data = [list_1, list_2, list_1, list_2]
data = np.array(data)
print("data = np.array( [list_1, list_2, list_1, list_2] ) , ", type(data))

print(data,"\nDonde además, podemos obtener los siguiente atributos\n")
print("data.shape -> ", data.shape)  # tamaño de la matriz
print("data.size -> ", data.size)   # numero de elementos total
print("data.ndim -> ", data.ndim)   # Numero de dimensiones
print("data.nbytes -> ", data.nbytes) # Bytes que emĺea para almacenar la información
print("data.dtype -> ", data.dtype, "\tNotemos que los arreglos sólo pueden tener un mismo tipo de elemento, no como las listas que podían tener lo que sea.") # Tipo de elemtnos que maneja

# Cómo menajar los tipos de las funciones
input('')
print("Los arreglos van a tener las siguientes opciones para almacenar:")
print("""
| `dtype` |                Variantes               |             Descripción           |
|---------|----------------------------------------|-----------------------------------|
|  `int`  |    `int8`, `int16`, `int32`, `int64`   |Enteros                            |
|  `uint` |  `uint8`, `uint16`, `uint32`, `uint64` |Enteros sin signo (no negativos)   |
|  `bool` |                `Bool`                  |Booleanos (`True` o `False`)       |
| `float` |`float16`,`float32`,`float64`,`float128`|Números de punto flotante          |
|`complex`|`complex64`, `complex128`, `complex256` |Números de punto flotante complejos|

y podemos especificar cómo se van a almacenar los elemnotos de un array, dada una lista.
Por default, los arreglos tienen elementos de tipo flotante.

""")
input('')

array_3 = np.array(list_1, dtype = np.int)
print("array_3 = np.array(list_1, dtype = np.int)\n\t-->",array_3)
array_3 = np.array(list_1, dtype = np.float)
print("array_3 = np.array(list_1, dtype = np.float)\n\t-->",array_3)
array_3 = np.array(list_1, dtype = np.complex)
print("array_3 = np.array(list_1, dtype = np.complex)\n\t-->",array_3)


input('')
# Aqui vemos cómo enermos que cambiar el tipo del elemento
print("Notemos que sólo se puede emplear dtype cuando se crea el arreglo, no después. Pero esto se puede solucionar creando una copia del arreglo:")
array_3 = np.array(array_3, dtype = np.int)
print("""array_3 = np.array(array_3, dtype = np.int)
array_3.dtype --> """,array_3.dtype  )

input('')
print('Como todas las operaciones en Python, al operar con dos tipos distintos, el resultado hereda el tipo \'más grande\':')
d1 = np.array([1, 2, 3], dtype=float)
d2 = np.array([1, 2, 3], dtype=complex)
print("""d1 = np.array([1, 2, 3], dtype=float)
d2 = np.array([1, 2, 3], dtype=complex)""")
print("(d1 + d2).dtype -->", (d1 + d2).dtype)


input('')
print('Por último, loa arreglos complejos funciones igual que los valores complejos usuales:')
print("d2.real", d2.real)
print("d2.imag", d2.imag)
