#! 1-strings-vs-characters.py

# En Python tenemos varias formas de guardar la información. Si nos interesa
# guardar la información de palabras o texto en general, el tipo de información
# se cataloga como strings (cadenas) o bien, como  caracteres.
# Equí estudiaremos la diferencia entre estos dos "tipos"

# Nota, en otros lenguajes es necesario decirle a la computadora qué tipo de información
# debe guardar una variable. En Python no es necesario hacerlo, sin embargo sí hay
# una nomenclatura especial.

# Hay tres formas de escribir variables de cadenas

# El caracter especial \n es un salto de línea.Hay otros como \t, \v, etc...
# En Python usar comillas simples (') o dobles (") es equivalente.
# Las cadenas con '' o " " sólo aceptan como contenido lo que esté en la misma línea
print("Primero saludemos muchas veces:")

str1 = 'Hola a todas y a todos.\nBienvenidos\n'
str2 = "Hola a todas y a todos.\nBienvenidos\n"
str3 = '''Hola a todas y a todos.
Bienvenidos
'''

# Las triples comillas (que son tres comillas simples o tres comillas dobles) y
# permiten incluir como string todo lo que está entre ellas, incluyendo saltos
# de línea o tabulaciones


strings = [str1, str2, str3]  # Esto es una lista, y hablaremos de ella más adelante
for i in strings:             # Esto es un ciclo for y hablaremos de ella más adelante
    print(i)                  # Sólo nota que pusimos una tabulación después del for

# Es usual para hablantes no anglosajones que muchos caracteres que se emplean
# no están disponibles en la porgramación, pero en eso depende de cómo
# esté codificado nuestra computadora

str4 = "Le di jalapeños a mi \U0001F436 y se enchiló."

print("Pero podemos poner textos más complejos:")
print(str4+ "\n")

# Esto ocurre porque empleamos el código UFT-8 (Unicode de 8 bits) que se puede
# extender hasta 16 bits, que es el caso para lo emojis y otros símbolos.

# Lo de los bits es la forma en la que la computadora procesa y guarada información
# pero para entrear en más detalles, hablemos de los caracteres

# Los caracteres son símplemente los elementes que conforman a nuestra cadenas
# para manipularlos tenemos que espefificar su posición considerando a la primera
# posición como la cero.

print( "Los elementos de las cadenas se llaman caracteres y podemos operar con ellos:")
print( "str1[0] = " + str1[0])
print( "str1[2:20] = " + str1[2:20])        # Podemos CONCATENAR cadejas si las "sumamos"
print("str1[0:-13] + \' \' + str4 = " +  str1[0:-13] + ' ' + str4) # Notemos que podemos agarrar
                                            # a los caracteres desde el incio al final
                                            # o del final al inicio (indicandolo con un signo menos)


# Operaciones con las cadenas y los caracteres

# Como se observó antes, podemos "sumar", concatenar cadenas. ¿Qué más se puede?
# Para más funciones ver Tabla 3.5 de Python Esential Reference 4th Edition
print("str4.upper() = ", str4.upper())
print("str1.swapcase()", str1.swapcase())


# Discutimos que los caracteres están representados en el unicode y que es información de
# 8 p 16 bits...¿Pero eso qué significa?
# Significa que hay 2^8 o 2^16 caracteres dinstintos que podemos identificar. Y la fomra
# de identificarlos es numerándolos... es decir que al final de cuentas los caracteres
# son número enteros! (y positivos)

# Y si so enteros, los podemos sumar, pero hay una pequeña diferencia en cómo lo hacemos
print("""Definamos las cadenas siguientes:
s_dog = '\\U0001F436'
num = '0123456789'
""")
s_dog = '\U0001F436'
num = '0123456789'


print("s_dog + num[0] = ", s_dog + num[0])
print("ord(s_dog) + ord(num[0]) = ", ord(s_dog) + ord(num[0]))

# Notemos que ord() nos da el entero asociado a un caracter, no a uns string.
# Si corrieramos el siguiete código nos daría un codemirror_mode
#
# ord(num)
#

# Hagamos una table de los valores que utilizamos con nuestras _cadenas_

print("\tCaracter\tValor\n"+
        "\t" + 25 * "-")                    # Notemos que también pudimos "multiplicar" la cadena, así como la sumamos
for s in s_dog + num:
    print("\t ", s, "\t\t", ord(s))
print("\t" + 25 * "-")         # Nota que la instrucción que no se
                                            # repite es la que no tiene una tabulación
