#! 1-booleanos.py
# Jonathan Urrutia
# 2022-02-21

# Los números booleanos
# Cualquier conjunto de dos elementos con los que podemos definir un álgebra (pensando en conjuntos)
# o en operaciones lógicas. Por eso tomaremos los valores de verdadero y falso.

var_1 = True
var_2 = False

print( 'var_1 = ', var_1, ', es de tipo ', type(var_1))
print( 'var_2 = ', var_2, ', es de tipo ', type(var_2))

# Lo usual es identificar al 0 con False, y al 1 con True, y al igual que los caracteres, también
# podemos pasarlos a números enteros y vice versa

print('\nDe entero a booleanos y viceversa:')

print('bool(1) = ', bool(1))
print('bool(0) = ', bool(0))
print('int(True) = ', int(True) )
print('int(False) = ', int(False))


# ¿Y esto funciona con strings?

print('\n¿Qué pasa con las strings?:')

true_string = 'cualquier cosa'
print('bool(' + true_string +') = ', bool(true_string), ' y es', type(bool(true_string)))

true_string = ''
print('bool(' + true_string +') = ', bool(true_string), ' y es', type(bool(true_string)))

# ¿De qué otras formas puedo obtener booleanos?
# Al realizar operaciones de comparacióncon relaciones matemáticas;

#
# |Operador|     Descripción   |  Ejemplo |
# |:------:|------------------ |:--------:|
# |  `==`  |     Igual que     | `x == 2` |
# |  `!=`  |   No igual que    | `2 != 3` |
# |   `<`  |    Mayor que      | `2 <  3` |
# |   `>`  |    Mayor que      | `3 >  2` |
# |  `<=`  | Menor o igual que |`3 <=  4` |
# |  `>=`  | Mayor o igual que |`5 >=  4` |


# Nos preguntamos si las dos variables son iguales, la respuesta es que no, por lo que var_1 será igual a False
print('\nDe la siguiente forma podemos obtener a los valores booleanos con relaciones de comparación:')

x = 8; y = 10
print('Si x = ', x,  'mientras que y = ', y)
var_1 = x == y
print( 'var_1 = x == y  ->  ', var_1, ' y es ', type(var_1) )

# Nos preguntamos si las dos variables son distintas, la respuesta es que no, por lo que var_1 será igual a False
var_1 = x != y
print( 'var_1 = x != y  ->  ', var_1, ' y es ', type(var_1) )

# Nos preguntamos si la primer variable es menor que la de la izquiera, la respuesta es que no, por lo que var_1 será igual a False
var_1 = x < y
print( 'var_1 = x < y  ->  ', var_1, ' y es ', type(var_1) )

# Nos preguntamos si la primer variable es mayor que la de la izquiera, la respuesta es que no, por lo que var_1 será igual a False
var_1 = x > y
print( 'var_1 = x > y  ->  ', var_1, ' y es ', type(var_1) )

# Nos preguntamos si la primer variable es mayor o igual que la de la izquiera, la respuesta es que no, por lo que var_1 será igual a False
var_1 = x <= y
print( 'var_1 = x <= y  ->  ', var_1, ' y es ', type(var_1) )

# Nos preguntamos si la primer variable es menor o igual que la de la izquiera, la respuesta es que no, por lo que var_1 será igual a False
var_1 = x >= y
print( 'var_1 = x >= y  ->  ', var_1, ' y es ', type(var_1) )

# Nos preguntamos si las dos variables son iguales, la respuesta es que no, por lo que var_1 será igual a False
x = 10; y = 10
print('\nSi x = ', x,  'mientras que y = ', y)
var_1 = x == y
print( 'var_1 = x == y  ->  ', var_1, ' y es ', type(var_1) )

# Nos preguntamos si las dos variables son distintas, la respuesta es que no, por lo que var_1 será igual a False
var_1 = x != y
print( 'var_1 = x != y  ->  ', var_1, ' y es ', type(var_1) )

# Nos preguntamos si la primer variable es menor que la de la izquiera, la respuesta es que no, por lo que var_1 será igual a False
var_1 = x < y
print( 'var_1 = x < y  ->  ', var_1, ' y es ', type(var_1) )

# Nos preguntamos si la primer variable es mayor que la de la izquiera, la respuesta es que no, por lo que var_1 será igual a False
var_1 = x > y
print( 'var_1 = x > y  ->  ', var_1, ' y es ', type(var_1) )

# Nos preguntamos si la primer variable es mayor o igual que la de la izquiera, la respuesta es que no, por lo que var_1 será igual a False
var_1 = x <= y
print( 'var_1 = x <= y  ->  ', var_1, ' y es ', type(var_1) )

# Nos preguntamos si la primer variable es menor o igual que la de la izquiera, la respuesta es que no, por lo que var_1 será igual a False
var_1 = x >= y
print( 'var_1 = x >= y  ->  ', var_1, ' y es ', type(var_1) )

# Finalmente, con los booleanos podemos hacer operaciones lógicas:

# Asignamos dos valores distintos
x = 8
y = 10

# Nos preguntamos si las dos variables son iguales, la respuesta es que no, por lo que var_1 será igual a False
test_1 = x == y  # Una forma equivalente es escribir: is
test_2 = x < y

print('\nOperaciones lógicas: and, or, not:\n')

print('test_1 = ', test_1)
print('test_2 = ', test_2, '\n')

print('not test_1 = ', not test_1)
print('test_1 and test_2 = ', test_1 and test_2)
print('test_1 or test_2 = ', test_1 or test_2)
print('not test_1 and test_2 = ', not test_1 and test_2)
print(  8 < 8 or 8 == 8, 8 <= 8)
