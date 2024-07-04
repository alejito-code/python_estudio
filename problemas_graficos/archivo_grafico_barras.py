import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pathlib
import numpy as np

ruta_script = pathlib.Path(__file__).parent 
ruta_archivo = ruta_script / 'fuente_ingresos.csv'

df = pd.read_csv(ruta_archivo)

sns.barplot(x='fuente',y='ingresos',data=df)

# Calculando total de ingresos
total_ingresos = df['ingresos'].sum()

# Calculando total a pesos colombianos
total_ingresos_pesos = total_ingresos * 4150  # tipo de cambio: 1 USD = 4150 COP

# Mostrando
print(f"El total de ingresos es de ${total_ingresos} y el valor de este a pesos colombianos es de ${total_ingresos_pesos:,}")

plt.show()