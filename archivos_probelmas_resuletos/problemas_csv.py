import pandas as pd
import pathlib

ruta_script = pathlib.Path(__file__).parent 
ruta_archivo = ruta_script / 'datos.csv'

df = pd.read_csv(ruta_archivo)

df["apellido"] = df['apellido'].astype(str) #mostramos la edad como str, llamamos solo un dato

print(df['apellido'][2]) 

#remplazar valores
df['apellido'] = df['apellido'].replace("rios","armas")

#eliminar filas con datos faltantes
df = df.dropna()

#eliminando filas repetidas
df = df.drop_duplicates()

df.to_csv(ruta_script / "datos_limpios.csv")

print(df)
