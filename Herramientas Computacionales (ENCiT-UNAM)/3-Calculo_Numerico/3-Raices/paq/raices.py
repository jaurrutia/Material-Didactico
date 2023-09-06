
import numpy as np

def root_int(f, x_list):
    '''
    Función que nos rergresa los interalos donde probablemente haya una raiz.
    f = función
    x_list es un np.array
    '''
    y = f(x_list)
    sign = np.zeros(len(y)-1)
    intervalos = []

    for i in range(0, len(sign)):
        sign[i] = y[i]*y[i+1]
        if sign[i] <= 0:
            intervalos.append([x_list[i], x_list[i+1]])

    return np.array(intervalos)

def bisection(f, int, tol = 1e-7, n_max = 1000, iteration_num = False):
    '''
    Metodo de biseccion para calcilar raices en un intervalo donde se
    garantice que hay una.
    f es una función
    int es una lista de dos elementos donde int[0]<int[1]
    '''
    count = 0
    x_left = int[0]
    x_right = int[1]
    delta_x = x_right - x_left
    mid_point = x_left + 0.5 * delta_x

    while (delta_x / 2 > tol and count < n_max):
        if f(x_left) * f(mid_point) > 0:
            x_left = mid_point
        elif f(mid_point) * f(x_right) > 0:
            x_right = mid_point
        else:
            break
        count += 1
        delta_x = x_right - x_left
        mid_point = x_left + 0.5 * delta_x
    if interation_num:
        return [mid_point, count]
    else:
        return mid_point

def secant(f, int, tol = 1e-7, n_max = 1000, iteration_num = False):
    '''
    Metodo de sección para calcilar raices en un intervalo donde se
    garantice que hay una.
    f es una función
    int es una lista de dos elementos donde int[0]<int[1]
    '''
    count = 0
    x_0 = int[0]
    x_1 = int[1]
    rts = x_0
    delta_x = -f(x_0) * (x_1 - x_0) / (f(x_1) - f(x_0))

    while (delta_x / 2 > tol and count < n_max):
        rts += delta_x
        x_0 = x_1
        x_1 = rts

        delta_x = -f(x_0) * (x_1 - x_0) / (f(x_1) - f(x_0))
        count += 1
    if iteration_num:
        return [rts, count]
    else:
        return rts

def newton_raphson(f, fprime, x_0, tol = 1e-7, n_max = 1000, iteration_num = False):
    '''
    Metodo de Newton-Raphson para el cálculo de raices. Es necesario definir:
    f es una función
    fprime es la derivada de la función a e entonctrar sus raices
    x_0 es un punto a evaluar la función
    '''
    x_i = x_0
    delta_x = -f(x_i) / fprime(x_i)
    x_i += delta_x
    count = 1

    while ( abs(delta_x) / 2 > tol and count < n_max):
        delta_x = -f(x_i) / fprime(x_i)
        x_i += delta_x
        count += 1
    if iteration_num:
        return [x_i, count]
    else:
        return x_i
