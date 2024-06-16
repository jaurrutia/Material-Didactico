

x = 3.1416325 / 4


sin = 0
factorial = 1
n = 8

i = 1
while i <= n:
    signo = (-1) ** (i + 1)
    sin = sin + signo * (x ** (2 *i - 1) )  / factorial
    factorial = factorial *(2 * i )*(2 *i + 1)
    i =  i + 1

n = 15
i = 1
sin = 0
factorial = 1
signo = -1
x_i = x
while i <= n:
    signo = signo * (-1)
    sin = sin + signo * x_i / factorial
    x_i = x_i * x * x
    factorial = factorial *(2 * i )*(2 *i + 1)
    i =  i + 1

print(sin - 2 ** (.5)/2.)
