"""Escribir un programa que almacene las asignaturas de
un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) 
en una lista, pregunte al usuario la nota que ha sacado en cada asignatura y
elimine de la lista las asignaturas aprobadas. Al final el programa debe
mostrar por pantalla las asignaturas que el usuario tiene que repetir.
"""

materias = ["matematica","fisica","quimica","historia","lengua"]

notas = []

#iterar sobre una copia de la lista materias
for i in materias.copy():
    nota = int(input(f"Cuanto a sacado en la materia de {i}: "))
    notas.append(nota)
    if nota >= 3:
        materias.remove(i)

print(f"Estas son las materias que necesita recuperar: {materias}")
