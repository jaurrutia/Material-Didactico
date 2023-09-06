
# Este paquete requiere de la bilbioteca math

from math import exp
from math import log

def minimos_cuadrados(x_list, y_list):
    '''minimos_cuadrados(x_list, y_list)\n
    Es el algoritmo que permite calcular la recta que mejor ajuste a un conjunto de datos asumiendo que tiene un comportamiento lineal.
    El valor que regresa es una lista que contiene la pendiente y la ordenada al orgien de dicha recta.
    La función requiere de dos listas de la misma longitud.
    '''
    if(len(x_list) != len(y_list) :
       return print("Las listas tienen longitudes distintas.")

    i = 0                                    # Contador
    S_x , S_xx , S_y , S_xy = 0 , 0 , 0 , 0  # Sumas de las expresiones de mínimos cuadrados, inicializadas en cero

    while i < len(x_list):                    # Para cada uno de los datos, opera las sumas
        S_x += x_list[i]
        S_xx += x_list[i] * x_list[i]
        S_y += y_list[i]
        S_xy += x_list[i] * y_list[i]
        i += 1
    n = i
    det = n * S_xx - S_x*S_x
    m = (n * S_xy - S_x * S_y) / det
    b = (S_xx * S_y - S_xy * S_x) / det
    return [m, b]


def minimos_cuadrados_potencia(x_list, y_list):
    '''minimos_cuadrados_potencia(x_list, y_list)\n
    Es el algoritmo que permite calcular la recta que mejor ajuste a un conjunto de datos asumiendo que  es una función de la forma
    y = a x ^n.
    El valor que regresa es una lista que contiene la potenciay el coeficiente de la función: [n, a]
    La función requiere de dos listas de la misma longitud.
    '''
    if(len(x_list) != len(y_list) :
       return print("Las listas tienen longitudes distintas.")


    i = 0                                    # Contador
    S_x , S_xx , S_y , S_xy = 0 , 0 , 0 , 0  # Sumas de las expresiones de mínimos cuadrados, inicializadas en cero

    while i < len(x_list):                    # Para cada uno de los datos, opera las sumas
        x = log(x_list[i])
        y = log(y_list[i])
        S_x += x
        S_xx += x * x
        S_y += y
        S_xy += x * y
        i += 1
    n = i
    det = n * S_xx - S_x*S_x
    m = (n * S_xy - S_x * S_y) / det
    b = (S_xx * S_y - S_xy * S_x) / det

    return [m, exp(b)]


def minimos_cuadrados_exponte(x_list, y_list):
    '''minimos_cuadrados_potencia(x_list, y_list)\n
    Es el algoritmo que permite calcular la recta que mejor ajuste a un conjunto de datos asumiendo que  es una función de la forma
    y = a x ^n.
    El valor que regresa es una lista que contiene la potenciay el coeficiente de la función: [n, a]
    La función requiere de dos listas de la misma longitud.
    '''
    if(len(x_list) != len(y_list) :
       return print("Las listas tienen longitudes distintas.")


    i = 0                                    # Contador
    S_x , S_xx , S_y , S_xy = 0 , 0 , 0 , 0  # Sumas de las expresiones de mínimos cuadrados, inicializadas en cero

    while i < len(x_list):                    # Para cada uno de los datos, opera las sumas
        x = x_list[i]
        y = log(y_list[i])
        S_x += x
        S_xx += x * x
        S_y += y
        S_xy += x * y
        i += 1
    n = i
    det = n * S_xx - S_x*S_x
    m = (n * S_xy - S_x * S_y) / det
    b = (S_xx * S_y - S_xy * S_x) / det

    return [m, exp(b)]
