#! 2-enteros.py
# Jonathan Urrutia
# 2022-02-22

# Librerias
# Ha operaciones matemáticas que no están definidas dentro de python, como las funciones
# trigonométricos, la raíz cuadrara, u otras. Para esto es que podemos emplear las
# librerias ya desrrolladas.

# Importemos la siguiente;
from math import  *
from cmath import *

print('''
from cmath import *
from math import *''')


# Notemos que de esta forma nosp permiteusar las funciones sin espicifar el método
print('pi = ', pi)

# Pero entonces no sabemos bien qué función estamos usando...
print( 'exp( pi * 1j) = ', exp( pi * 1j))
