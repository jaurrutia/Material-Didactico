
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.sin(3*x)+np.cos(2*x)*(np.sin(-9*x)+np.cos(9*x))

def dv_num(func,int,h): # int = [a, b]
    x = int[0]
    x_list = []
    fprime = []
    while x < int[1]:
        x_list.append(x)
        fprime.append( (func(x + h) - func(x)) / h )
        x += h
    return [x_list,fprime]

def dv_num_list(func, xlist):
    fprime = []
    for i in range(0,len(xlist)-1):
        h = xlist[i+1] - xlist[i]
        fprime.append( (func(xlist[i+1]) - func(xlist[i])) / h )
    return [xlist[:-1],fprime]

def dv_num_list_back(func, xlist):
    fprime = []
    for i in range(1,len(xlist)):
        h = xlist[i] - xlist[i-1]
        fprime.append( (func(xlist[i]) - func(xlist[i-1])) / h )
    return [xlist[1:],fprime]

def dv_num_list_cen(func, xlist):
    fprime = []
    weight = [.5 , -.5]
    for i in range(1,len(xlist)-1):
        h = xlist[i] - xlist[i-1]
        fprime.append( (weight[0] * func(xlist[i+1]) + weight[1] * func(xlist[i-1])) / h )
    return [xlist[1:-1],fprime]

def dv_num_list_cen_4(func, xlist):
    fprime = []
    weight = [-1/12. ,2./3. , -2./3. , 1/12.]
    for i in range(2,len(xlist)-2):
        h = xlist[i] - xlist[i-1]
        fprime.append( (weight[0] * func(xlist[i+2]) + weight[1] * func(xlist[i+1]) +  weight[2] * func(xlist[i-1])  + weight[3] * func(xlist[i-2])) / h )
    return [xlist[2:-2],fprime]


x = np.linspace(0,2*np.pi, 100)
y = f(x)
# yprime = np.cos(x)
[x_num, yprime_num] = dv_num(f, [0, 2*np.pi] , .1)
#[x_num_1, yprime_num_1] = dv_num_list(f, x)
#[x_num_1b, yprime_num_1b] = dv_num_list_back(f, x)
[x_num_2c, yprime_num_2c] = dv_num_list_cen(f, x)
[x_num_4c, yprime_num_4c] = dv_num_list_cen_4(f, x)


#plt.plot(x,yprime, marker = '*', label = r"$f'(x)$ - Analitica")
plt.plot(x, np.zeros(len(x)))
plt.plot(x,y, marker = '*', label = r'$f(x)$')
#plt.plot(x_num, yprime_num, marker = '.', label = r"$f'(x)$ - Num (1)")
#plt.plot(x_num_1, yprime_num_1, marker = '.', label = r"$f'(x)$ - Num (1) - list")
#plt.plot(x_num_1b, yprime_num_1b, marker = '.', label = r"$f'(x)$ - Num (1) - list-b")
plt.plot(x_num_2c, yprime_num_2c, marker = '.', label = r"$f'(x)$ - Num (2) - list-c")
plt.plot(x_num_4c, yprime_num_4c, marker = '.', label = r"$f'(x)$ - Num (4) - list-c")




plt.legend()
plt.show()
