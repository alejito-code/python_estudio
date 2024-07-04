import time
import os

#creamo un bulce infinto
while True:
    hora = time.strftime("%H:%M:%S")#traemos los datos que necesitamos
    os.system("cls")#limpiamos la consola 
    print(f"La hora exacta es: {hora}")#imprimimos hora
    time.sleep(1)#utilizamos el .sleep para que se pause por un segundo
    
"""el bucle consiste en que cada vez que se limpie la consola y se uase el .sleep se muestre la hora actual cada vez y asi da el efecto de reloj"""