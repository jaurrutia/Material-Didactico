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
                   # i es el numero con el que iremos recorriendo los elementos de string
i = 1
num_final = 0       # Este es el valor que iremos sumando para tner el número decinal
potencia = 1        # la potencia, o el lugar dnde está el dígito actualmente potencia = 0 son unidades, por ejemplo
while i < len(string)+1:  # Mientas nuestro índice sea uno válido string, empezando desde el final
    digit = ord(string[-i])  # empezamos por el ultimo lugar de la string porque estas son las unidades
    if ord('0') <= digit and digit <= ord('1') :    # Si nuestro caracter está entre los digitos arábigod
        digit = ( digit - ord('0'))     # Lo pasamos a su vaor numeric a partir del lugar del unicode
        num_final += potencia* digit    # Lo multiplicamos opr su potecia ed 10
        potencia = 2 * potencia                   # Pasamos al siguiente lugar de las potencias
    else:
        print(string[-i], 'No es un número')      # Si no es un numero, nos lo saltamos
    i+=1        # Pasamos al siguiente caracter

print(num_final, type(num_final))
