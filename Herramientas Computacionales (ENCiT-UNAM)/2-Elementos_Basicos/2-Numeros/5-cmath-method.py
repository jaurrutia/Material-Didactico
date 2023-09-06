#! 2-enteros.py
# Jonathan Urrutia
# 2022-02-22

# Librerias
# Ha operaciones matemáticas que no están definidas dentro de python, como las funciones
# trigonométricos, la raíz cuadrara, u otras. Para esto es que podemos emplear las
# librerias ya desrrolladas.

# Importemos la siguiente;
import cmath        # Estas funciones nos ayudan a exetnder math nuestros cálculos para valores complejos

print("cmath.pi = ", cmath.pi ) # Todas las funciones o varibales del paquete van a ser llamadas con math.<elemento>.
                              # Al prefijo se le conoce como el `método` ya que hace referencia a una biblioteca particular.

# De esta forma, no sólo tenemos cálculo más rápidos que los usual, sino que en algunos casos con mayor presición
print("cmath.exp( math.pi * 1j) = ", cmath.exp( cmath.pi * 1j)  )

input('')
z = 1. + 0.5 * 1j
print("z = ", z)

z_polar = cmath.polar(z)
print("cmath.polar(z) = ", z_polar)
print("cmath.rect((z_polar[0],z_polar[1]) = ", cmath.rect(z_polar[0],z_polar[1]))

print('¿Puedo calcular la idnetidad de Euler?')
input('')
print('cmath.exp( cmath.pi * 1j)', cmath.exp( cmath.pi * 1j))
