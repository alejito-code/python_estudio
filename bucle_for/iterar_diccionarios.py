diccionario = {
    "nombre" : "Alandro",
    "apellido" : "Rios",
    "edad" : 18
}

#iterando con for (key solo mostrara la key)
for key in diccionario:
    print(key)
print("--------")

#iterando con for (usando el metodo items para mostrar todo con valor y etc...)
for datos in diccionario.items():
    indice = datos[0]
    valor = datos[1]
    print(f"La llave es: {indice} y el dato de esta es: {valor}")
    