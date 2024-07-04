numeros = [2,4,6,8]

numeros_2 = [451,895,1544,45,1215,1515,114]

#encontrando el mayor de una lista
numero_mayor = max(numeros)
print(numero_mayor)

print("--------")
#encontrando el menor de una lista
numero_menor = min(numeros)
print(numero_menor)

#redondeando a 6 números
numero = round(58.95145,98)

#devuelve false a = 0 o dato vacio si dato cadena numero etc devuelve true
dato_bool = bool(0)

#comprueba si todos los datos son verdaderos(no buena practica ya que si un solo dato false, devuelve false tood el iterable)
dato_all = all([4587,"True","pandevono",[458,"r"]])

sumando = sum(numeros_2)

print("--------")
print(sumando)
