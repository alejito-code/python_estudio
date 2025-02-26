"""Definir una funcion inversa() que calcule la inversion de una oracion"""

def inversa(cadena):
    return cadena[::-1]

cadena = input("Ingrese una oracion y yo se la volteo (se volteo el titanic): ")
resultado = inversa(cadena)

print(f"Su oracion volteada es igual a: {resultado}")