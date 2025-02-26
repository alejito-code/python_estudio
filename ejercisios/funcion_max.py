"""definir funcion max que tome como argumento dos numeros 
y devuelva el mayor de ellos"""

def max (num1, num2):
    if num1 < num2:
        print(f"{num1} es mayor que {num2}")
    else:
        print(f"{num2} es mayor que {num1}")
   
numero1 = input("Ingrese el primer numero: ")
numero2 = input("Ingrese el segundo numero: ")

resultado = max(numero1, numero2)

print(resultado)
