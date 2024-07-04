ingreso_mensual = 10

if ingreso_mensual >= 10000:
    print("vives bien en cualquiere parte del mundo")
    
elif ingreso_mensual >= 1000:
    print("vives bien en latino america")
    
elif ingreso_mensual >= 500:
    print("vives bien en colombia")
    
elif ingreso_mensual >= 50:
    print("vives bien en venezuela")
    
else:
    print("""pobre hijueputa""")    
    
ingreso_mensual = 1000000
consumo_mensual = 10000

if ingreso_mensual <= 1000:
    print("eres pobre")
    
elif ingreso_mensual - consumo_mensual == 0:
    print("te lo estas gastando todo pendejo")
    
elif ingreso_mensual - consumo_mensual <= 25000:
     print("estas gastando bien")
        
elif ingreso_mensual - consumo_mensual <= 50000:
     print("estas gastando adecuadamente")
        
else: print("todo correcto mi afafacho")