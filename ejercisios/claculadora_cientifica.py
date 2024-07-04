""""Escribir una función que simule una calculadora científica que permita calcular
el seno, coseno, tangente, exponencial y logaritmo neperiano. La función preguntará
al usuario el valor y la función a aplicar,y mostrará por pantalla una tabla con los
enteros de 1 al valor introducido y el resultado de aplicar la función a esos enteros."""

import math

def calculadora_cientifica():
    # Preguntar al usuario el valor máximo y la función a aplicar
    valor_maximo = int(input("Ingrese el valor máximo: "))
    print("Seleccione la función a aplicar:")
    print("1: Seno")
    print("2: Coseno")
    print("3: Tangente")
    print("4: Exponencial")
    print("5: Logaritmo Neperiano")
    opcion = int(input("Ingrese el número de la función (1-5): "))
    
    # Definir la función a aplicar basada en la opción del usuario
    if opcion == 1:
        funcion = math.sin
        nombre_funcion = "Seno"
    elif opcion == 2:
        funcion = math.cos
        nombre_funcion = "Coseno"
    elif opcion == 3:
        funcion = math.tan
        nombre_funcion = "Tangente"
    elif opcion == 4:
        funcion = math.exp
        nombre_funcion = "Exponencial"
    elif opcion == 5:
        funcion = math.log
        nombre_funcion = "Logaritmo Neperiano"
    else:
        print("Opción inválida.")
        return
    
    # Imprimir la tabla de resultados
    print(f"\nTabla de {nombre_funcion}")
    print(f"{'Número':<10}{nombre_funcion:<20}")
    print("-" * 30)
    
    for i in range(1, valor_maximo + 1):
        try:
            resultado = funcion(i)
            print(f"{i:<10}{resultado:<20}")
        except ValueError as e:
            print(f"{i:<10}{'Error: ' + str(e):<20}")

# Llamar a la función para ejecutarla
calculadora_cientifica()
