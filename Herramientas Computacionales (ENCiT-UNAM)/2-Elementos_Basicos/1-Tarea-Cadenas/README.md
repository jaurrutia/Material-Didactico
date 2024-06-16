# Tarea 1: Cadenas y enteros

## Nombre:

## Calificación:

En clase comenzamos a trabajar con las cadenas y vimos que los caracteres, que son los elementos que transforman a los caracteres, son entereos al final de cuenta. Adicionalmente, vimos que hay funciones que pueden operar sobre las cadenas para modificarlas y tener algún tpo de información de éstas. En esta tarea, trabajaremos los dos elemeentos aprendidas para comenzar a delegar tareas mecánicas a la computadora mediante python.

## Instrucciones

Archivos entregables: **tres archivos PY**.

1. Escribe un algoritmo equivalente a la función `int()`, donde el usuario introduzca una cadena de númenros enteros decimales, y regerse una variable tipo entero. Nombre a tu archivo **1-string2int.py**.

  - No puedes emplear la función `int()` dentro de tu código.

2. Crea un algoritmo para que el usuario introduzca un número entero en base decimal y le regrese una cadena ed caracteres en su representación binaria y la pueda imprimir con un formato `string_decimal, string_binarios`. Llama a tu archivo **2-dec2bin.py**.

  - Para este paso sí puedes usar `int()`
  - Considera que el entero que se le da a la máquina es menor a $2^8-1$ y mayor a cero.

3. Crea un algoritmo para que el usuario introduzca un número entero en base binaria y le regrese una cadena de caracteres en su representación decimal y la pueda imprimir con un formato `string_binarios, string_decimal`. Llama a tu archivo **3-bin2dec.py**.

  - Para este paso sí puedes usar `int()`
  - Considera que el entero que se le da a la máquina es menor a $2^8-1$ y mayor a cero.

4. Crea un código para que Python lea un archivo y lea cuántos caracteres de espacios (espacio, salto de linea y tabulaciones) y palabras hay, y que calcule la longitud de las palabras (entendiendo una palabar como cualquier cosa entre espacios en blanco). Al final tu archivo debe imprimir un diagrama de frecuencias de las longitudesde palabras y espacios. Llama a tu archivo **4-frecuencias.py**

  - Puedes hacer una prueba con el archivo adjunto.

### Hint:

Revisa los códigos de ejemplos vistos en clase. Recuerda los comados de bash:

> pyton3 codigo.py < test_file.txt > output.txt

## Evaluación

- [ ] 1-string2int.py
- [ ] 2-dec2bin.py
- [ ] 3-bin2dec.py
- [ ] 4-frecuencias.py
