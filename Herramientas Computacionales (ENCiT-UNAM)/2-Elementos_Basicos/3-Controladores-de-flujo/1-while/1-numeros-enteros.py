# 1-numeros-enteros.py
# 2022 - 03 -03
# Herramientas computacionales, ENCiT

# Este script imprime los numeros enteros desde el 0, hasta un numero n dado

n = int(input("Dame un número entero: ")) # Creamos un entero a partir de una string dada

i = 0       # Iniciamos el contador en cero
list = []   # Creamos una lista vacía donde vamos a almacenar cada número

while i <= n:       # Mientras el contador (i) sea menor que la cota superior (n), haz lo siguiente:
    list.append(i)  # Alamcenamos el valor de (i) en nuestra lista, (append = concatenar)
    i = i + 1       # Aumentamos el contador en una unidad

print(list)         # Imprime la lista
