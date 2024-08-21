#! 3-for-def.property

# Definamos la función que me regresa los primeros n enteros


def int_list(n):
    i = 0
    list = []
    while i <= n:
        list.append(i)
        i = i + 1
    return list

def suma_enteros( n ):
    sum = 0
    for i in int_list(n):
        sum = sum + i
    return sum


i = 0
n = 8

while i <= n:
    sum = suma_enteros(i)         # Imprime la lista
    print(sum, i * ( i +1 )//2 )
    i = i + 1
