import pathlib
import csv

ruta_script = pathlib.Path(__file__).parent # buscamos la ruta en la que nos encontramos en este momento
ruta_archivo = ruta_script / 'datos.csv' # le añadimos a la ruta la ruta donde se encuentra el archivo

with open(ruta_archivo, 'r') as tablas:
    archivo = csv.reader(tablas)
    for row in archivo:
        print(row)