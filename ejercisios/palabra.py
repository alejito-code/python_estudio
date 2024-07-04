""""Escribir un programa que pida al usuario una palabra
y luego muestre por pantalla una a una las letras de la palabra
introducida empezando por la última."""

palabra = input("ingrese una palabra: ").lower()

letra = []

for i in palabra:
    letra.append(i)
    

letra.reverse()    
print(letra)