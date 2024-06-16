
import numpy as np
import matplotlib.pyplot as plt # Un paquete de graficos

def func(m, n):
    return n + 10 * m

A = np.fromfunction(func, (6, 6), dtype=int)
print("A = np.fromfunction(func, (6, 6), dtype=int)")
print(A)
fig, ax = plt.subplots()
ax.imshow(A)
ax.set_title('np.fromfunction')
plt.show()

A = np.identity(6, dtype=int)
print('A = np.identity(6, dtype=int)')
print(A)
fig, ax = plt.subplots()
ax.imshow(A)
ax.set_title('np.identity(6)')
plt.show()

A = np.eye(6, dtype=int)
print('A = np.eye(6, dtype=int)')
print(A)
fig, ax = plt.subplots()
ax.imshow(A)
ax.set_title('np.eye(6)')
plt.show()

A = np.eye(6, dtype=int, k = 2)
print('A = np.eye(6, dtype=int, k = 2)')
print(A)
fig, ax = plt.subplots()
ax.imshow(A)
ax.set_title('np.eye(6, k = 2)')
plt.show()

A = np.eye(6, dtype=int, k = -1)
print('A = np.eye(6, dtype=int, k = -1)')
print(A)
fig, ax = plt.subplots()
ax.imshow(A)
ax.set_title('np.eye(6, k = -1)')
plt.show()

A = np.logspace(0, 2, 50)
A = np.diag(A)
print('''A = np.logspace(0, 2, 50)
A = np.diag(A)''')
print(A)
fig, ax = plt.subplots()
ax.imshow(A)
ax.set_title(' np.diag(A)')
plt.show()
