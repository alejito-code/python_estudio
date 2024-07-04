"""Escribir un programa
en el que se pregunte al usuario por una frase y una letra, y
muestre por pantalla el número de veces que aparece la letra en la frase."""

frase = input("Escribe cualquier frase a continuación: ").lower()

letra = input("Ingrese la letra que desea buscar en el anterior texto: ").lower()

contador_letra = 0
for i in frase:
    if i == letra:
        contador_letra += 1

print(f"La {letra} esta {contador_letra} en la frase que nos diste") 