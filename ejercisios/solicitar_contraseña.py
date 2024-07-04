"""Escribir un programa que almacene la cadena de caracteres contraseña en una variable,
pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta."""

import sys

contraseña = input("Ingrese una contraseña (anótela en alguna parte para que no se le olvide): ")
contraseña2 = input("Ingrese su contraseña de nuevo: ")

if contraseña != contraseña2:
    print("Las contraseñas no coinciden, inténtelo otra vez")
    sys.exit()
else:
    acceso = input("Ingrese su clave de acceso: ").lower()
    contador_de_intentos = 0
    while contraseña != acceso:
        contador_de_intentos += 1
        if contador_de_intentos < 3:
            print("Las contraseñas no coinciden")
            acceso = input("Intentelo de nuevo: ").lower()
        else:
            print("Llamando a la policia")
            sys.exit()
    print("¡Su clave es correcta, bienvenido!")