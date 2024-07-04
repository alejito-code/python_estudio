"""
%H: hora en formato de 24 horas (00-23)
%I: hora en formato de 12 horas (01-12)
%M: minutos (00-59)
%S: segundos (00-59)
%d representa el día del mes (01-31)
%B representa el nombre del mes (enero, febrero, marzo, etc.)
%Y año

"""
import datetime

fecha_actual = datetime.datetime.now()#tomamos la fecha actual
dia_y_mes = fecha_actual.strftime("%d %B %Y")#tomamos de esta solo mes y dia 
hora = fecha_actual.strftime("%I: %M: %S")

print(f"{dia_y_mes} y la hora es: {hora}")