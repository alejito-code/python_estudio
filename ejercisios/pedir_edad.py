"""Escribir un programa que pregunte al usuario su edad y muestre por
pantalla todos los años que ha cumplido (desde 1 hasta su edad). MODIFICACION:
obtendremos el año actual y basandonos en este le dirimos al usuario
en que año vivio cada edad"""

import datetime

año_actual = datetime.datetime.now().year

edad = int(input("Ingrese su edad en numero: "))

for i in range(1, edad + 1):
    año_vivido = año_actual - (edad - i)
    print(f"En el año {año_vivido} tenías {i} años")