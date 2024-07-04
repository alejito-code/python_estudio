frutas = ["banana","manzana","pera","durazno","mango","granadilla"]
cadena = "quibo gonorrea"
numeros = [2,4,6,8]
#idenracion pero saltando alguna cosa, pidienqo eu no la muestre usando (sentencia  continue) 
for fruta in frutas:
    if fruta == "pera":
        continue
    print(f"Me gusta la/el: {fruta}")
    
print("--------")
#usando la sentencia break para parar totalmente el bucle (sentencia BREAK)(si usamos break todo lo que este despues de este tambien termina osea no se muestra )
for fruta in frutas:
    print(f"Me gusta la/el: {fruta}")
    if fruta == "pera":
        break
    
print("---------")    
for letra in cadena:
    print(letra)
    
print("---------")
#for en una sola lina de codigo
numeros_operaciones = [x*2 for x in numeros]
print(numeros_operaciones)