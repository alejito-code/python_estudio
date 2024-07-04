def frase(nombre,apellido,adjetivo):
    return f"Hola {nombre} {apellido}, sos muy {adjetivo}"

frase_resultado = frase(nombre="Alejandro",adjetivo="Estupido",apellido="Ríos")
print(frase_resultado)

#si lo definimos desde arriba quedara definido por defecto a no ser que le pasemos el parametro y este cambie, si no quedara el que tiene por defecto