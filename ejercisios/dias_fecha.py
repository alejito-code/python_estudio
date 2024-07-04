import datetime

def calcular_fecha_pasada(dias):
    fecha_actual = datetime.datetime.now()
    fecha_pasada = fecha_actual - datetime.timedelta(days=dias)
    return fecha_pasada

dias_pasados = 880
fecha_pasada = calcular_fecha_pasada(dias_pasados)
print("La fecha que era hace", dias_pasados, "días fue:", fecha_pasada)
