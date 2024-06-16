#! 2-enteros.py
# Jonathan Urrutia
# 2022-02-22

# Los números flotantes
# Python interpreta a los fotantes como un número que tega un punto decimales

entero = 1
flotante = 1.  # Ya con este cambio, tenemos un flotante

print('x = ', entero, ' cumple con que', type(entero))
print('x = ', flotante, ' cumple con que', type(flotante))

string_value = '1.5'  # Si este fuese el input de una variable, podríamos pasarlo a un valor flotante rápidamente con `float()`
float_value = float(entero)
print('float( entero ) --->', float_value, type(float_value))

float_value = float(string_value)
print('float( \'1.5\') --->', float_value, type(float_value))



# Los números complejos
# Python interpreta a los complejos como un número que tega la letra j
input('')
z = 3 + 5j
print('z = ', z, type(z))

# Podemos emplear a los `atributos` de estas variables (no confundir con los métodos) para agarrar la parte real o imaginaria del complejo
print('z.real = ',z.real, 'y es tipo: ', type(z.real))  # Notemos que al escribira a la unidad imaginaria, nuestra variable toma un tipo flotante en cada una de sus entradas
print('z.imag = ',z.imag, 'y es tipo: ', type(z.imag))

x = 1.  # Un flotante
print('\nx = ', x, 'con tipo', type(x))
print(  "complex(x) = ", complex( x ))
print(  "complex(x, 5) = ", complex( x, 5 )) # Le puede poner otro argumento


input('')
# Operacionees aritméticas con estos operadores

print('Así es como podemos obteneer a los números complejos a partir de los flotantes o enteros')
print('(-1) ** (.5) = ', (-1) ** (.5) )   # equivalente a (-1)^(.5) = (-1)^(1/2) = sqrt(-1) = i


input('')
euler = 2.718281828459045;
pi = 3.141592653589793
print('''Definamos algunos valoers constantes:
euler = 2.718281828459045
pi = 3.141592653589793''')

print('\nFórmula de Euler: e^(i Pi) = -1')
print('euler ** (1j * pi ) = ', euler ** (1j * pi ))
