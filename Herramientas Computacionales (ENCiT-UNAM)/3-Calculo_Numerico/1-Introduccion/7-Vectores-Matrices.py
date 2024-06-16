
import numpy as np
import matplotlib.pyplot as plt # Un paquete de graficos

# Veamos cómo podes modificar arreglos y entenderlos
print('Veamos cómo modificar a los arreglos:')

ex = np.array([[1, 2], [3, 4]])
print('ex = np.array([[1, 2], [3, 4]])')
print(ex)
print( 'np.reshape(ex, (1, 4))\n', np.reshape(ex, (1, 4))  )
print( 'ex.reshape(4)\n', ex.reshape(4) )
input('')

a = np.linspace(1, 10, 12)
print('a = np.linspace(1, 10, 12)')
print(a)
print('a.reshape((3,2,2))',a.reshape((3,2,2)))
input('')

data = np.array([[1, 2], [3, 4]])
print('data = np.array([[1, 2], [3, 4]])')
print(data)
print('data.flatten()', data.flatten() )
print( 'data.flatten().shape', data.flatten().shape )
input('')

data = np.arange(0, 5)
print('data = np.arange(0, 5)')
print(data)
column = data[:, np.newaxis]  # Agregamos una dimensión más
row = data[np.newaxis, :]
print('''column = data[:, np.newaxis]
row = data[np.newaxis, :]  ''')
print(column)
print(row)
input('')

data1 = np.arange(1, 6)
data2 = np.arange(2, 7)
print('''data1 = np.arange(1, 6)
data2 = np.arange(2, 7)''')
print('np.vstack((data, data1, data2))\n',np.vstack((data, data1, data2)))
print('np.hstack((data, data1, data2))\n',np.hstack((data, data1, data2)))
print('np.hstack((data[:, np.newaxis], data1[:, np.newaxis], data2[:, np.newaxis]))\n',np.hstack((data[:, np.newaxis], data1[:, np.newaxis], data2[:, np.newaxis])))
input('')


A = np.array([[11, 12, 13], [21, 22, 23], [31, 32, 33]])
v = np.array([1, 2, 3])
u = np.array([[1], [2], [3]])
print('''
A = np.array([[11, 12, 13], [21, 22, 23], [31, 32, 33]])
v = np.array([1, 2, 3])
u = np.array([[1], [2], [3]])''')
print('A + v \n', A + v)
print('A + u \n', A + u)
input('')

x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6], [7, 8]])
print("""x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6], [7, 8]])""")
print( "x + y\n", x + y )
print( "y - x\n", x - y )
print( "y * x\n", x * y )
print( "y / x\n", x / y )
print( "2 * x\n", 2 * x )
print( "x **2\n", x **2 )
input('')
