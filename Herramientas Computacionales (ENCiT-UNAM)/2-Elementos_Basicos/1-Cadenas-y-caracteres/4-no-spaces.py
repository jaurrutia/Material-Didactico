#! 4-no-scapes.py
#
# En códigos anteriores vimos que hay unas funciones que aplican sobre cadenas
# que se escriben con la sintexis
#       <cadena>.<funcion>(<argumentos>)
# auqnue esto es muy útil, es bueno entender cómo funciona el algoritmo
# para realizar procesos

# Escribiremos una versión propioa de la función que cambia todas
# las letras a mayúsculas, sacando privecho del Unicode
#

string = input()

# Delimitadores de palabras
blank = ' '
tab = '\t'
comma = ','
nline = '\n'
point = '.'

my_string = ''         # Creemos una cadena vacía que llenaremos poco a poco
my_list = []            # Creemos una lista vacía donde guardaremos nuestras palabras

inside_word = True      # Definamos una varible que me diga si estoy en una palabra
outside_word = False    # y una si estamos fuera
status = False    # Y una de status, y supongamos que no estamos en una palabra

i = 0                   # i es el numero con el que iremos recorriendo los elementos de string
s = string[i]           # Cada uno de los caracteres
while i < len(string)-1:
    if(s != blank  and s != tab):    # Si no son espacios
        status = inside_word                        # Estamos dentro de la palabra
        my_string += s                              # Vamos llenandola
    else:     # Si son espacios en blanco
        status = outside_word                       # Estamos fuera de una palabra, entonces guardamos la palabra
        my_list.append(my_string)                   # La almacenamos en una lista
        my_string  = ''                             # Reseteamos la cadena
    i += 1              # Pasamos al siguiente caracter
    s = string[i]       # Pasamos al siguiente caracter

my_string += s                         # El último ya no lo almacenamos. Entonces lo ponemos afuera del loop
my_list.append(my_string)              # Almacenamos

i = 0;                  # Imprimimos el resultado
#print(my_list)
while i < len(my_list):
    print(my_list[i] + ' ', end = '')
    i += 1
