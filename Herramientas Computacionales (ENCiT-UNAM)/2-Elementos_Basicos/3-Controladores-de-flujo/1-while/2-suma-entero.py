# 1-numeros-enteros.py
# 2022 - 03 -03
# Herramientas computacionales, ENCiT

# Este script imprime los numeros enteros desde el 0, hasta un numero n dado

n = int(input("Dame un número entero: ")) # Creamos un entero a partir de una string dada

suma = 0
i = 0       # Iniciamos el contador en cero

while i <= n:        # Mientras el contador (i) sea menor que la cota superior (n), haz lo siguiente:
#    print (i)       # Imprime le número del contador
    suma = suma + i  # Aumentamos el valor de i a la varibale sum
    i = i + 1        # Aumentamos el contador en una unidad

print( suma )
