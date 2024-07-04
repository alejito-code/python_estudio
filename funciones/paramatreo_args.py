#utilizando args
def suma(nombre,*numeros):
    return f"{nombre}, la suma de tus numeros es: {sum(numeros)}"

resultado = suma("Alejandro",48,51,4,2,1,5,18,)
print(resultado)