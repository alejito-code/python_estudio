import pathlib

ruta_script = pathlib.Path(__file__).parent # buscamos la ruta en la que nos encontramos en este momento
ruta_archivo = ruta_script / 'pandevono.txt' # le añadimos a la ruta la ruta donde se encuentra el archivo

with open(ruta_archivo, 'r') as archivo: # abrimos el whit y abrimos el archivo con r para ser leido 
    linea = archivo.readline() # llamamos por linea
    
    lineas = archivo.readlines() # llamamos por lineas
    # print(archivo.read()) /leemos el archivo completo/ 
    print(linea) # leemos por lineas 