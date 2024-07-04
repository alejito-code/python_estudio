"""Escribir un programa que pida al usuario un número entero
y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido."""

#pedimos un numero al usuario
num = int(input("Digite un numero entero: "))

#cresamos un for in range para que tome cada numero y en un print imprimimos multiplicando * por range de vecez 
for i in range(1, num + 1):
    print("*" * i)