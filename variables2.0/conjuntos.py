#creando un conjunto con set
conjunto = set(["dato1"])

#metiendo un conjunto dentro de otro conjunto
conjunto1 = frozenset(["dato2","dato3"]) #congelamos el conjunto para hacerlo manipulable
conjunto2 = {conjunto1,"dato45"}#concatenamos para llamar ambos conjuntos ya que el conjunto1 esta congelado con (frozenset)


print(conjunto2)

#teoria de conjuntos
conjunto1 = {1,2,3,4}
conjunto2 = {4,2}

#verificando si es un subconjunto
resultado1 = conjunto2.issubset(conjunto1)
resultado2 = conjunto2 <= conjunto1

#verificando si es un super conjunto
resultado1 = conjunto2.issuperset(conjunto1)
resultado2 = conjunto1 > conjunto2

#verificando si hay numeros que coinciden en los  dos conjuntos
resultado1 = conjunto2.isdisjoint(conjunto1)

print(resultado1)
print(resultado2)  