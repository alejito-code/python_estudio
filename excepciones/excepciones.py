def sumar():
    while True:
        a = input("Ingresa un numero: ")
        b = input("Ingresa un numero: ")
        try:
            resultado = int(a) + int(b)
            break
        except:
            print("Te pedi un numero no tus mamadas de chistes de mierda hijo de puta sidoso")
    return resultado

print(sumar())