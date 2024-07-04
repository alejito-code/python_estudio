#pedir al usuario que ingrese una palabra y esta imprimirla diez vecez

palabra = input("ingrese una palabra: ").lower()
vecez = 0

for i in range(0,11):
    vecez+= 1
    print(f"esta es su palabra {palabra} {vecez} vecez repetida")
