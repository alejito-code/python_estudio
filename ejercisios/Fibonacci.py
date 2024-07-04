"""Crea un algoritmo para la sucesión de Fibonacci. La sucesión de Fibonacci es la siguiente serie:

 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89"""
 
n = 100
fib = [0, 1]
for i in range(2, n):
    fib.append(fib[i-1] + fib[i-2])

print(fib)