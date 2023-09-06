


suma_todos = 0
suma_pares = 0
suma_impares = 1

n = 10
for i in range(0, n + 1):
    suma_todos = suma_todos + i
    suma_pares = suma_pares +  2 * i
    suma_impares = suma_impares + ( 2 * i - 1)

print( [suma_todos, suma_pares, suma_impares] )
