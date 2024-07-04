"""
funcion que nos devuelva números primos hasta
llegar a un número primo especifico
"""
def numeros_primos_hasta(numero):
    primos = []
    for i in range(2, numero + 1):
        es_primo = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                es_primo = False
                break
        if es_primo:
            primos.append(i)
    return primos

print(numeros_primos_hasta(159))