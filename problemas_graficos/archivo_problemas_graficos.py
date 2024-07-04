import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pathlib

ruta_script = pathlib.Path(__file__).parent 
ruta_archivo = ruta_script / 'porro.csv'

df = pd.read_csv(ruta_archivo)

sns.lineplot(x='fecha',y='pedos',data=df)

plt.plot(1, 16, 'o')
plt.plot(5, 17, 'o')
plt.plot(10, 18, 'o')
plt.plot(3, 12, 'o')
plt.plot(11, 12, 'o')

plt.show()