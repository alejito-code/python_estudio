total = 0
productos=[]
while True:
    producto = input("Nombre de producto: ") #pedimos el producto
    productos.append(producto) #almacenamos los productos en la lista antes guardada vacia
    cantidad = int(input("Cantidad del prodcuto: ")) #pedimos la cantidad y la convertimos en entero
    precio = float(input("Precio del producto: ")) #pedimos el precio y convertimos a float
    subtotal=round(cantidad * precio) #multiplicamos de una vez el precio por la cantidad
    total+=subtotal #almacenamos los totales para que los vaya sumando
    continuar = input("Presionar X para calcular o enter para continuar: ") #preguntamos al usuario sii desea ingresar otro producto
    print("----------")

    if continuar == "X": #imprimimos todo
        IVA = total * 0.19
        print("Productos: ", productos)
        print("----------")
        print("Precio total: ", total)
        print("----------")
        print(f"Este es el precio con el IVA {total + IVA}")
        print("----------")
        break
    

