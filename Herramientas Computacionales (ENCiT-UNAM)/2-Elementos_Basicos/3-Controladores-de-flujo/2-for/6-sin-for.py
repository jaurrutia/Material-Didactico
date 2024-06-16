x = 3.1416325 / 4

sin = 0
factorial =1
sigo = -1
x_i = 1

for i in range(1, 8):
    signo = signo * (-1)
    sin = sin + signo * x_i / factorial
    x_i = x_i * x * x
    factorial = factorial *(2 * i )*(2 *i + 1)
        
