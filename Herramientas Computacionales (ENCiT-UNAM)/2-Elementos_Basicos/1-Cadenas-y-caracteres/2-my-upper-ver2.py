#! 2-my-upper.py
#
# En códigos anteriores vimos que hay unas funciones que aplican sobre cadenas
# que se escriben con la sintexis
#       <cadena>.<funcion>(<argumentos>)
# auqnue esto es muy útil, es bueno entender cómo funciona el algoritmo
# para realizar procesos

# Escribiremos una versión propioa de la función que cambia todas
# las letras a mayúsculas, sacando privecho del Unicode
#

string = input("Dame una cadena:")

# Recordemos en el únicode los caracteres están ordenados y cada uno tiene un
# número entero asociado. Vamos a ignorar la dependencia con los acentos. Entonces, proponemos:

my_string = ""          # Creemos una cadena vacía que llenaremos poco a poco
i = 0                   # i es el numero con el que iremos recorriendo los elementos de string
while i < len(string):  # Mientas nuestro índice sea uno válido string
    num = ord(string[i])
    if (ord('a') <= num and num <= ord('z')) or  (ord('à') <= num and num <= ord('ü')):    # Si nuestro caracter está entre las minúsculas
        num = num - (ord('a') - ord('A'))   # Desplazamos el número la misma distancia que hay entre las mayúsculas y las minúscula
        my_string = my_string + chr(num)    # char() nos da el caracter en unicode correspondiente, y y lo concatenamos en my_st
    else:
        my_string += string[i]
    i += 1              # Pasamos al siguiente caracter

print(my_string)
