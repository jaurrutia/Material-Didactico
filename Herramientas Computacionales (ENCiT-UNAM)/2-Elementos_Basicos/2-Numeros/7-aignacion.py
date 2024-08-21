n = input('Dame un número entero: ')
n = int(n)  # vaor inicia
bin_rev = ''  # cadena en sentido inverso de su representacion binaria
bin = ''   # cadena eel orden correcto de ls represetnacion binaria
digit = None # Digito actual a gardar en bin_rev de las rtŕesentaion biaria


while n > 0:
    digit = n % 2
    bin_rev += str( digit ) # x += 1  x = x + 1
    n //=  2 #  n = n // 2

i = len(bin_rev) - 1
while i >= 0:
    bin += bin_rev[i]
    i -= 1
print('Su repersentación binaria es:', bin)

i = 0
n = 0
power = 1
while i < len(bin_rev):
    digit = int(bin_rev[i])
    n += power * digit
    power *= 2
    i += 1
print('Y con esta vemos que el numero era:', n)
