lista = [480,45,12,1,6,4,8,3,9,4,15,3,5456]

#creando funcion lamdba
multiplicar_numero = lambda x : x*2

#funcion para saber si un numero es par
def par(num):
    if (num%2==0):
        return True
    
#uasndo filter como especie de bucle (filter ejecuta cada dato uno por uno haciendo lo que se le ordena, semi bucle)
numeros_pares = filter(par,lista)

#creando lo mismo que lo anterior pero con lambda
numeros_pares_2 = filter(lambda numero:numero%2 == 0,lista)

print(list(numeros_pares_2))

