""""Escribir un programa que pida al usuario un número entero positivo
y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas."""

# Solicitar al usuario que ingrese un número entero positivo
numero = int(input("Ingrese un número entero positivo: "))

# Verificar que el número ingresado es positivo
if numero <= 0:
    print("El número debe ser un entero positivo.")
else:
    # Inicializar una lista para almacenar los números impares
    numeros_impares = []

    # Usar un bucle para encontrar los números impares desde 1 hasta el número ingresado
    for i in range(1, numero + 1):
        if i % 2 != 0:
            numeros_impares.append(str(i))

    # Unir los números impares con comas y mostrarlos por pantalla
    print(", ".join(numeros_impares))

