#! 2-my-lower.py
# Jonathan Urrutia
# 2022-02-21
# ENCiT, Herramientas computacionales I
#
# Modificación de ../2-my.upper.py para simular a la operación
#
#       string.lower()
# que cambia mayúsculas por minúsculas

string = input("Dame una cadena:")

# Recordemos en el únicode los caracteres están ordenados y cada uno tiene un
# número entero asociado. Vamos a ignorar la dependencia con los acentos. Entonces, proponemos:

my_string = ""          # Creemos una cadena vacía que llenaremos poco a poco
i = 0                   # i es el numero con el que iremos recorriendo los elementos de string
while i < len(string):  # Mientas nuestro índice sea uno válido string
    num = ord(string[i])
    if ord('A') <= num and num <= ord('Z'):    # Si nuestro caracter está entre las mayúsculas
        num = num - (ord('A') - ord('a'))   # Desplazamos el número la misma distancia que hay entre las mayúsculas y las minúscula
        my_string = my_string + chr(num)    # char() nos da el caracter en unicode correspondiente, y y lo concatenamos en my_string
    elif ord('À') <= num and num <= ord('Ü'):  # Por como está el ´unicode, me permite hacer este cambbio u extener el my_lower_py a estos caracteres
        num = num - (ord('À') - ord('à'))
        my_string = my_string + chr(num)
    else:
        my_string += string[i]              # Si es un caracter de otro tipo, sólo lo ponemos
    i += 1              # Pasamos al siguiente caracter

print(my_string)
