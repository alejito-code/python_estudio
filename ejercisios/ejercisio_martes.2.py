def generate_invoice():
    total = 0
    cantidades = []
    frutas = []
    valores = []
    
    while True:
        nombre = input("Cual es su nombre (completo): ")
        cedula = input("Ingrese su cedula: ")
        producto = input("Ingrese la fruta: ")
        frutas.append(producto)
        cantidad = int(input("Cantidad del producto: "))
        cantidades.append(cantidad)
        precio = float(input("Precio del producto: "))
        valores.append(precio)
        subtotal = round(cantidad * precio)
        total += subtotal
        
        continuar = input("Presionar 'x' para calcular o enter para continuar: ")
        if continuar.lower() == "x":
            IVA = total * 0.19
            print("-----FACTURA-----")
            print(nombre)
            print("----------")
            print(cedula)
            print("----------")
            print("Frutas compradas: ", frutas)
            print("----------")
            print(f"Estos son los precios que lleva: {valores}")
            print("----------")
            print(f"Estas son las cantidades que lleva: {cantidades}")
            print("----------")
            print("Precio total: ", total)
            print("----------")
            print(f"Este es el precio con el IVA {total + IVA}")
            print("-----SIGUIENTE FACTURA-----")
            break
    
    return total

num_facturas = int(input("Ingrese el número de facturas que desea imprimir: "))
for factura in range(num_facturas):
    print(f"FACTURA {factura + 1}")
    total_factura = generate_invoice()
