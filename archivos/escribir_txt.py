import pathlib

ruta_script = pathlib.Path(__file__).parent 
ruta_archivo = ruta_script / 'mio_amore.txt' 

with open(ruta_archivo, 'w', encoding="UTF-8") as archivo:
    for i in range(100000):
        if i % 100 < 50:
            archivo.write(" " * (i % 100) + f"feliz cumple amor mio, TE AMO {i}\n")
        else: 
            archivo.write(" " * (100 - (i % 100)) + f"feliz cumple amor mio, TE AMO {i}\n")