"""creamos una funcion y luego la ejecutamos"""

def saludar(nombre):
    print(f"Hola {nombre}, buenas")
    
saludar("Alejandro")

"""funcion para sumar"""

def suma(a,b):
    calculo = a - b
    print(f"Le llevas a tu hermano {calculo}")
    
suma(75,32)

"""pedir los valores para la funcion"""

nombre = input("Digite su nombre a continuacion: ")
edad = int(input("Digite su edad: "))
edad2 = int(input("Digite la de su hermano: "))

saludar(nombre)
suma(edad,edad2)

#crear una funcion que nos retorne valores
def crear_contraseña_random(num):
    chars = "abcdefghij"
    num_entero = str(num)
    num = int(num_entero[0])
    c1 = num - 2
    c2= num
    c3 = num - 5
    contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}"
    return contraseña

password = crear_contraseña_random(18)
frase = f"Tu contraseña nueva es: {password}"
print(frase)
    