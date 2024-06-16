#! 2-enteros.py
# Jonathan Urrutia
# 2022-02-22

# Biblioteca
# Ha operaciones matemáticas que no están definidas dentro de python, como las funciones
# trigonométricos, la raíz cuadrara, u otras. Para esto es que podemos emplear las
# bliobetcas y a desrrolladas.

# Importemos la siguiente;
import math         # `wrappers` de C  de para usar en python
import cmath        # Estas funciones nos ayudan a exetnder nuestros cálculos para valores complejos

print("math.pi = ", math.pi ) # Todas las funciones o varibales del paquete van a ser llamadas con math.<elemento>.
                              # Al prefijo se le conoce como el `método` ya que hace referencia a una biblioteca particular.
print("math.e = ", math.e )

# De esta forma, no sólo tenemos cálculo más rápidos que los usual, sino que en algunos casos con mayor presición
print("math.sqrt(25) = ", math.sqrt(25))
print("25 ** (.5) = ", 25 ** (.5) )

print("math.exp(10) = ", math.exp(10))
print("math.e ** (10) = ", math.e ** (10))
print("math.cos(math.pi) = ", math.cos(math.pi) )

print('¿Puedo calcular la idnetidad de Euler?')
input('')
math.exp( math.pi * 1j) # Pero no funcionan estas funciones con números complejos...
