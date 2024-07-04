#creando diccionario con dict()
diccionario = dict(nombre="lucas",apellido="rios")

diccionario1 = dict.fromkeys("ABCDEF","rios")

#creando un diccionario vacio con fromkeys (es un metodo por lo tanto debemos llamar primero al dict, deja los espasios en none)
diccionario = dict.fromkeys(["alejo","rios"])

print(diccionario1)
print(diccionario)