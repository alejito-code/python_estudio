nombres = ["alejandro","rios","carodna"]
numeros = [23,14,25]

"""for num in numeros:
    print(f"La variables numeros cambia cada vez y el numero es: {num}")"""

print("--------")    
for num in numeros:
    resultado = num * 10
    print(f"La variable almacenada multiplicada por diez es iguala a: {resultado}")

else :
    print("Se acabo el bucle for")
    
print("--------")
# iterar dos listas usando el metodo sict
for nomb,num in zip(numeros,nombres):
    print(nomb)
    print(num)

print("--------")
#iterar con rango
for num in range(10,12):
    print(num)
    
#recorrer una lista con indice    
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f"El inice es: {indice} y el numero es: {valor}")
    
# TODO LO ANTERIOR FUNCIONA DE LA MISMA MANERA CON LAS TUPLAS