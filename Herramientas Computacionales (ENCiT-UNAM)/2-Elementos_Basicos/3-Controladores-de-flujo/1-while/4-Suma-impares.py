#! 4-Suma-impares

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

def suma_impares(n):
    i = 1
    suma = 0
    while i <= 2 * n:
        suma = suma +  i
        i = i + 2
    return suma

def suma_pares(n):
    i = 0
    suma = 0
    while i <= 2 * n:
        suma = suma +  i
        i = i + 2
    return suma

def suma_impares_pares(n):
    i = 0
#    suma_todos = 0
    suma_pares = 0
    suma_impares = 0
    while i <= 2 * n:
        suma_pares = suma_pares +  i
        i = i + 1
        suma_impares = suma_impares + i
        i = i + 1
    return [suma_pares, suma_impares]

def suma_todos_impares_pares(n):
    i = 0
    suma_todos = 0
    suma_pares = 0
    suma_impares = 1
    while i <= n:
        suma_todos = suma_todos + i
        suma_pares = suma_pares +  2 * i
        suma_impares = suma_impares + ( 2 * i - 1)
        i = i + 1
    return [suma_todos, suma_pares, suma_impares]

n = 10

print(suma_enteros(n), suma_pares(n), suma_impares(n))
print(suma_todos_impares_pares(n))


'''
n = 8
i = 0
suma = 0

while i <  n:
    suma = suma +  (2* i  + 1)
    i = i + 1

print(suma)
#######################

n = 8
i = 1
suma = 0

while i <=  n:
    suma = suma +  (2* i  - 1)
    i = i + 1

print(suma)
'''
####################################

n = 8
i = 0
suma = 0

while i <= 2 * n:
    suma = suma +  i
    i = i + 2

print(suma)
