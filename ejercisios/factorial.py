"""crea un programa que pida un numero y devuelva la factorial de este
una factorial es tomar todos los numeros antes de ese y multiplicarlo por el numero """


def factorial_iterativo(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

numero = int(input("Introduce un número para calcular su factorial: "))
print(f"El factorial de {numero} es {factorial_iterativo(numero)}")
