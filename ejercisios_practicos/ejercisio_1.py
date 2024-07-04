#promedio de duracion de los videos
otros_cursos_min = 2.5 
otros_cursos_max = 7
otros_cursos_prom = 4
curso_rios = 1.5

#diferencia de duraciom
diferencia_min = 100 - (curso_rios / otros_cursos_min * 100) #restado para hallar la diferencia
diferencia_max = 100 - (curso_rios * 1000 // otros_cursos_max / 10) #truco para quitar decimales, multiplicamos para alargar usamos(//) luego restamos 
diferencia_prom = 100 - (curso_rios / otros_cursos_prom * 100) #restado para hallar la diferencia
print("------------------")
print(f"El curso de Rios dura un {diferencia_min}% menos que el mas rapido")
print(f"El curso de Rios dura un {diferencia_max}% menos que el mas lento")
print(f"El curso de Rios dura un {diferencia_prom}% menos que el promedio de todos los cursos")
print("------------------")

print(f"Ver 10 horas de este curso equivale a {otros_cursos_prom * 100 // curso_rios / 10} horas mas de otros cursos") 
print(f"Ver 10 horas de otros cursos equivale a {curso_rios * 100 // otros_cursos_prom / 10} horas menos de curso Rìos") 
print("------------------")