import pandas as pd
import pathlib

ruta_script = pathlib.Path(__file__).parent 
ruta_archivo = ruta_script / 'datos.csv'

df = pd.read_csv(ruta_archivo)
df2 = pd.read_csv(ruta_archivo)

# Obteniendo los datos de una columna especifica
nombres = df["edad"]

# Ordenando dato s
df_ordenado = df.sort_values("edad")

# ordenadno de fomr a desendente
df_ordenado = df.sort_values("edad",ascending=False) # si usamos false ordenamos al reves

# concatenando los dos datafrems
df_concatenado = pd.concat([df,df2])

# accediendo a la primer fila 
primer_fila = df.head(1)

# accediendo a la ultimas filas
primer_fila = df.tail(1)

# accediendo a la cantidad de filas y columnas con shape
filas,columnas = df.shape

#obteniendo data estaditica
df_info = df.describe()

#accediendo a un elemento especifico del df con loc
elemento_especifico = df.loc[2,"edad"]

#accediendo a un elemento especifico del df con iloc por id
elemento_especifico_2 = df.iloc[2,1]

#accedemos a todas las filasd de una columna con loc
apellidos = df.loc[:,"edad"]

#accedemos a todas las filasd de una columna con iloc
apellidos_2 = df.iloc[:,1]

#accedemos a las filas mayores de : numero tal
filas_mayor_a_15 = df.loc[df["edad"]>15,:]

print(filas_mayor_a_15) 