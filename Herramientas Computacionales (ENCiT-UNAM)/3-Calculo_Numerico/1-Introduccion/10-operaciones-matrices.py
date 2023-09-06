
import numpy as np

print('Para arreglos N - dimensionales, con numpy podemos sacar provecho de las siguentes funciones:')
print('''
|   Función   |       Descripción                            |
|-------------|----------------------------------------------|
|`dot`|Multiplicación de matrices (producto escalar) entre dos arreglos dados que representan vectores, matrices o tensores|
|`inner`|Multiplicación escalar (producto interno) entre dos arreglos que representan vectores|
|`cross`|El producto cruz entre dos arreglos que representan vectores|
|`tensordot`|Producto escalar a lo largo de ejes específicos de arreglos multidimensionales|
|`outer`|Producto externo (producto tensorial de vectores) entre dos arreglos que representan vectores|
|`kron`|Producto de Kronecker (producto tensorial de matrices) entre arreglos que representan matrices y arreglos de dimensiones superiores|
|`einsum`|Evalúa la convención de suma de einstein para matrices multidimensionales|
''')
input('')

A = np.arange(1, 7).reshape(2, 3)
B = np.arange(1, 7).reshape(3, 2)
print('A = np.arange(1, 7).reshape(2, 3)\nB = np.arange(1, 7).reshape(3, 2)')
print(A)
print(B)
print('np.dot(A,B) --->', np.dot(A,B)  )
print('np.dot(B,A) --->', np.dot(B,A)  )
input('')

print('Podemos utilizar dot, para calcular operaciones de vectores con matrices:')
A = np.arange(9).reshape(3, 3)
x = np.arange(3)
print('''A = np.arange(9).reshape(3, 3)
x = np.arange(3)''')
print('np.dot(A, x) ---> ', np.dot(A, x) )
print('A.dot(x) ---> ', A.dot(x))
input('')

print('¿Cuál es la diferencia de inner y dot?')
A = np.array([[1,2],[3,4]])
B = np.array([[11,12],[13,14]])
print('''A = np.array([[1,2],[3,4]])
B = np.array([[11,12],[13,14]])
''')
print('np.dot(A,B) --->',np.dot(A,B))
print('np.inner(A,B) --->',np.inner(A,B))
input('')


print('¿Y el producto exterior?')
x = np.array([1, 2, 3])
print('x = np.array([1, 2, 3])')
print('np.outer(x, x)--->', np.outer(x, x))
input('')

print('¿Y el producto cruz?')
x = np.array([1,0,0])
y = np.array([0,1,0])
print('''x = np.array([1,0,0])
y = np.array([0,1,0])''')
print('np.cross(x, y)--->', np.cross(x, y))
