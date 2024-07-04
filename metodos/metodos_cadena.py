cadena1 = "hola soy rios"
cadena2 = "154266591"

#UPPER mayusculas
resultado = cadena1.upper()

#lOWER minusculas 
resultado2 = cadena2.lower()

#CAPITALIZE primera en mayuscula y el resto en miniscula
resultado3 = cadena1.capitalize()

# #FIND busqueda de cadenas dento de una cadena(sin resltado devuelve -1, cuenta esapacios y desde 0)
resultado4 = cadena2.find("9")

#INDEX bucqueda de cadenas dentro de una cadena(sin resultado devuleve error, resto igual a FIND)
resultado5 = cadena2.index("2")

#ISNUMERIC si es umerico devuelve true 
resultado6 = cadena1.isnumeric()

#usando slising 
cadena = "0123456789"
print(cadena[:5]) 

print(resultado5)