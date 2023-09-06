#! 2-enteros.py
# Jonathan Urrutia
# 2022-02-22

# Los números enteros
# Python interpreta a los enteros con cualuiqera delas siguientes sintaxis:

x = 0
print('x = 0 --> ', type(x))  # Sin puntos decimales

x = 5684518651
print('x = 5684518651 --> ', type(x))

# Para enteros de varias cifras la siguiente notación resula muy cómoda para enteros, que nos permite dividir en potencias de 10^3
x = 5_684_518_651
print('x = 5_684_518_651 --> ', type(x))

# Pasando de strings a int

age = input("Dame tu edad:")
age_num = int(age)
print('La mitad de tu vida tuviste fue cuando tenías', int(age) // 2, 'años.')  # Cabe destacar que empleamos la operación de división por entero `//`
                                                                                # en lugar de la división simple `/` esto se debe a que cuando hablamos
                                                                                # de edades, nunca nos referimos a medios número, sino a enteros.

# Para enteder por qué está definida esta operación, analicemos primero cómo  se ejecutan el resto de operaciones y después, analicemos cómo la computadora
# entiende a los números enteros.

input('')
a = 98
b = 5
c = 843
print("\nHagamos\n a = ", a, "; b = ", b, "; c = ", c,";\n")
ans = a + b
print('a + b = ', ans, ' y es tipo ---> ', type(ans) )

ans = a - b
print('a - b = ', ans, ' y es tipo ---> ', type(ans) )

ans = a * c
print('a * c = ', ans, ' y es tipo ---> ', type(ans) )

ans = a * (b - c)
print('a * (b - c) = ', ans, ' y es tipo ---> ', type(ans) )

ans = a ** b                  # En el caso en el que b >= 0, la potencia es otra forma de escribir una multiplicación por lo que siguie siendo una operación cerrada para este caso
print('a ** b = ', ans, ' y es tipo ---> ', type(ans) )


input('')
a = 27
b = 3
c = 4
print("\nHagamos\n a = ", a, "; b = ", b, "; c = ", c,";\n")

ans = a / b   # A pesar de que 27 / 3 = 9, que es un número entero, la división `/`arroja un resultado flotante (9.0). Como veremos más adeltante eso tiene consecuencias en el uso de memoria
print('a / b = ', ans, ' y es tipo ---> ', type(ans) )

ans = a // b  # Si en cambio utilizo la división entera, me da el mismo resultado pero ahora sí obtenemos un número entero como resultado: 9
print('a // b = ', ans, ' y es tipo ---> ', type(ans) )

ans = a % b   # La operación módulo siempre regresa un entero, dado que nos calcula el residup de la división a / b, como 27 sí es divisible entre 3, sobran cero
print('a % b = ', ans, ' y es tipo ---> ', type(ans) )



ans = a / c   # En este caso, 27 no es divisible entre 4, por lo que el uso de la división con sus decimales es correcto (un flotante, pues)
print('\na / c = ', ans, ' y es tipo ---> ', type(ans) )

ans = a // c   # Y con el operador de divsión entera lo que obtenemos es un entero... lo que es  incorrecto matemáticamente pues ignora a los decimales, de hecho se observa que sólo
               # se queda la parte entera de la operación (ni siquiera hace un redonde)
print('a // c = ', ans, ' y es tipo ---> ', type(ans) )

ans = a % c   # En este caso, el .75, corresponde a 3/4, que es el cociente entre el residuo y el divisor, por lo tanto el módulo de a y c es 3
print('a % c = ', ans, ' y es tipo ---> ', type(ans) )
