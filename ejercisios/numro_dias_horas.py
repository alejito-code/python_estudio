"""Escribir un algoritmo que, para cualquier número de segundos inferior 
a un millón, calcule su equivalente en días, horas, minutos y segundos."""

# Pedimos datos.
dato = input(u'Número de segundos: ')

# Hacemos un cast, convirtiendo la cadena en un número largo.
dato = float(dato)

# Comprobamos si el número introducido es menor a un millón.
if dato >= 1000000:
    print ("El número debe de ser menor a 1000000")
else:
    # Días.
    ndias, aux = divmod(dato, 86400)
    # Horas.
    nhoras, aux = divmod(aux, 3600)
    # Minutos y segundos.
    nmin, nseg = divmod(aux, 60)
    # Mostramos resultado.
    print ('%d días, %d horas, %d minutos, %d segundos' % \
          (ndias, nhoras, nmin, nseg))