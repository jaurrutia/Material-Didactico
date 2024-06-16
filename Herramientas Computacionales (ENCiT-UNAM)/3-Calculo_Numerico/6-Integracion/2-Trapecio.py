
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.sin(x)

def y(x):
    return x**2 + 3*x + 1

def int_simpson_def( func, int, dx = 0.001):
    res = 0
    x = np.arange(int[0], int[1], dx)
    i = 0
    while i < len(x):
        res += (func(x[i]-dx/2) + func(x[i] + dx/2))* 0.5 * dx
        i += 1
    return res

def int_simpson( func, int,  dx = 0.001, y_0 = 0):
    x = np.arange(int[0], int[1], dx)
    res = 0
    sol = np.zeros(len(x))  # sol = []
    i = 0
    while i < len(x):
        res += (func(x[i]-dx/2) + func(x[i] + dx/2))* 0.5 * dx
        sol[i] = res  # sol.append(res)
        i += 1
    return [np.array(x), np.array(sol) + y_0]

int = [0,np.pi*2]
print(int_simpson_def(f, int))




fig, axs = plt.subplots(2, figsize=(8,8), sharex = True, gridspec_kw={'height_ratios': [1, 3]})
axs[0].grid(True)
axs[1].grid(True)

axs[1].set_xlabel(r"$x\;\; $",fontsize = 15)
axs[0].set_ylabel("Error",fontsize = 15)
axs[1].set_ylabel(r"$\int\sin(x)dx$",fontsize = 15)


int = [0,6]
[x, sol] = int_simpson(y, int, y_0 = 0, dx = .1)
analitico = x*x*x /3+ 3*x*x/2.+ x
#[x, sol] = int_simpson(f, int, dx = .05 , y_0 = -1)
#analitico = -np.cos(x)
axs[1].plot(x, f(x), lw = 3, color = 'r', label = r'$f(x) = \sin(x)$')
axs[1].plot(x, analitico,   lw = 3,  label = r'$f(x) = \cos(x)$')
axs[1].plot( x, sol, '.',  lw = 3, label = r'$f(x)_{Riemann} $')

axs[0].plot(x, analitico-sol, '.-',  lw = 3)
#plt.plot(x,y, marker = '*', label = r'$f(x)$')


plt.legend()
plt.show()
