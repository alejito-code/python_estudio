# Solicitar al usuario un número entero
num = int(input("Ingrese un número entero: "))

# Imprimir el triángulo rectángulo
for i in range(1, num*2, 2):
    for j in range(i, 0, -2):
        print(j, end=' ')
    print()
