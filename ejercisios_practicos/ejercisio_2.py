#solicitamos frase
frase = input("Dime una frase y te calculo el tiempo: ")
#separamos las palabras de los espacios (usando una lista)
palabras_separadas = frase.split(" ")
#contamos las palabras
cantidad_palabras = len(palabras_separadas)
#hacemos el reclamos por durar mas de un minuto (120 palabras = 1min)
print("------------")
if cantidad_palabras > 120:
    print("relajao papi, tampoco me cuentes tu vida crack")
print("------------")
print(f"dijiste {cantidad_palabras} palabras, y tardarìas {cantidad_palabras/2} segundos en decirlo")
print(f"Dalto lo diria en {cantidad_palabras * 100 // 2 *1.3 / 100} segundos")

