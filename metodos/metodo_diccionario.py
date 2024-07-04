diccionario = {
    "nombre" : 'lucas',
    "apellido" : 'rios',
    "edad" : 18
}

#mostrando los keys (tambien sirve para iterar)
claves = diccionario.keys()

#buscando valor por la key
valor = diccionario.get("apellido")

print(valor)