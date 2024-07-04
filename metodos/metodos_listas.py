#creamos una lista usando list ( no es un buen uso pero si es buen uso para crear listas vacias)
lista = list ({234,23})

#imprime en pantalla la cantiadd de elementos de la lista
resultado = len(lista)

#agregando elemntos a la lista (modificando directamente la lista)
lista.append(True)

#agregando elemento a la lista (posicion especifica)
lista.insert(2,12)

#agregando una lista a la lista (para agregar varios elementos)
lista.extend({45,True, False ,24})

#eliminando elemntos por el indice
lista.pop(2) # NOTA -1 para eliminar el ultimo -2para eliminar el penultimo y asi sucesivamente

#remviendo elemntos de la lista por su valor (busqueda, si no encuentra arroja error)
lista.remove(23)

#ordena de manera asendente sin strings (false y true de primero y los numeros despues)(si usamos el reverse los ordena en reversa)
lista.sort()

#invirtiendo la lista sin esatr ordenada 
lista.reverse()

#usando reep paras ver las veces que hay un mismo dato
rep = ["hola" , 3 , True , 3 , 3 , "pandevono"]
print(rep.count(3))
print(lista) 