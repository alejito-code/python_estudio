import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pathlib

ruta_script = pathlib.Path(__file__).parent 
ruta_archivo = ruta_script / 'dispercion.csv'

df = pd.read_csv(ruta_archivo)

sns.scatterplot(x='tiempo',y='dinero',data=df)

plt.show()