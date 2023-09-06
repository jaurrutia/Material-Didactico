# 4-passing_arguments.py
# Jonathan Urrutia
# Last modification: 2022-02-03

# Este es una modificación del 'Hola, Mundo' para poder pasar argumentos directamente al  programa sin necesidad de que nos pregunte uno por uno.

# Paara esto necesitamos usar una función de Python que no viene por default, sin embargo está en una 'biblioteca' la cual podemos llamar.
# si queremos correr este 'script' en la términal podemos poner el siguiente código
# 	python3 name_of_script.py argumento1 argumento2 
#

from sys import argv  # De la biblioteca llamada 'sys' vamos a importar la función 'argv'

user_name, best_friend = argv[1], argv[2]  #argv es un arreglo que podemos llamar para declarar nuevas variables

print( "Hello, World!" )
print("Hello, ", user_name)
print("Hello, ", best_friend)


# Para este script empleamos algunos términos y funciones nuevas que veremos más a detalle en futuras clases.
