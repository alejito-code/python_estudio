"""Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10."""

for i in range(1, 11):
    print("------------------------------")
    for n in range(1, 11):
        resultado = i * n
        print(f"{i} x {n} = {resultado}")