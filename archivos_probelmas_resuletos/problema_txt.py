nombres = ["Juana","Alejandro","Pandevono","Danniella","Chimuelo"]
apellidos = ["Betancur","Ríos","Buñuelo","Armas","Sanz"]

with open("nombres_apellidos.txt","w", encoding="UTF=8") as arch:
    arch.write("Los datos son:\n")
    for n, a in zip(nombres, apellidos):
        arch.write(f"Nombre: {n}\nApellido: {a}\n----------\n")
    arch.write("Gracias por usar nuestro servicio de escribir txt")