#pide un numero y arroja como resultado la tabla de multiplicar de este
n = int(input("Dame un numero: "))

for i in range(1,11):
    print(f"{n} x {i} = {n*i}")
    