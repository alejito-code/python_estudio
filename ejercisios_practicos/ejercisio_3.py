#importamos libreria para hacer modf
import datetime
import locale

#configuramos el idioma predeterminado si es ingles usamos US
locale.setlocale(locale.LC_ALL, 'es_ES')

#pedir el nombre y la edad de los compañeros que vinieron hoy a clase.
def obtener_compañeros(cantidad_de_compañeros):
  compañeros = []
  for i in range(cantidad_de_compañeros):
    nombre = input("ingrese el nombre del compañero: ")
    edad = int(input("ingrese la edad del compañero: "))
    compañero = (nombre, edad)
    compañeros.append(compañero)
  fecha_actual = datetime.datetime.now()#tomamos la fecha actual
  dia_y_mes = fecha_actual.strftime("%d de %B")#tomamos de esta solo mes y dia 
  compañeros.sort(key=lambda x: x[1])
  asistente = compañeros[0][0]
  profesor = compañeros[-1][0]
  return asistente, profesor, compañeros, dia_y_mes

asistente, profesor, compañeros, dia_y_mes = obtener_compañeros(3)
print(f"El profesor es: {profesor} y su asistente es {asistente}")
print(f"Estos son los compañeros que vinieron el dia del {dia_y_mes}:{compañeros}")