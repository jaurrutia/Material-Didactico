#! 5-factorial.py

# n! = n  * (n -1 ) * (n - 2) * ... * (1) * 0!
# 0! = 1

n = 4
i = 1
factorial = 1;

while i <= n:
    factorial = factorial * i
    i =  i + 1
print(factorial)

factorial = 1
i = n
while i >  0:
    factorial = factorial * i
    i =  i  - 1
print(factorial)
