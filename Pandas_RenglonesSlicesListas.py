import pandas as pd 
import random
SEPARADOR = ("*" * 20) + "\n"

#Creación de un DataFrame a partir de un diccionario
diccionario_notas_aleatorias = { \
   "Crescencio":[random.randrange(60,101) for x in range(3)], \
   "Domitila":[80,100,57], "Rutilio":[80,70,57], "Pánfilo":[20,100,100], \
   "Lodoviko":[100,100,100]} 
notas = pd.DataFrame(diccionario_notas_aleatorias)
notas.index = ["Programación", "Base de datos", "Contabilidad"]

#Accesar renglones utilizando slices
#IMPORTANTE:En este formato, el final del slice SI está incluido
print("Todas las asignaturas, todos los estuduiantes")
subConjunto = notas.loc["Programación":"Contabilidad"]
print(subConjunto)
x = input("Presiona una tecla")


print(SEPARADOR)

print("Últimas dos asinaturas, todos los estudiantes")
subConjunto = notas.loc["Base de datos":"Contabilidad"]
print(subConjunto)
print(SEPARADOR)

#Accesar subconjuntos de renglones y columnas
print("Subconjunto, solamente las notas de Rutilio y Lodoviko para las primeras dos asignaturas")
subConjunto = notas.loc["Programación":"Base de datos", ["Rutilio","Lodoviko"]]
print(subConjunto)
print(SEPARADOR)

#Indexado booleano
print("Solamente calificaciones aprobatorias")
aprobados = notas[notas >= 70]
print(aprobados)
print(SEPARADOR)

print("Solamente calificaciones aprobatorias entre 70 y 80")
aprobados = notas[(notas >= 70) & (notas <= 80)] #DEBE utilizar &
print(aprobados)
print(SEPARADOR)

print("Solamente calificaciones NO aprobatorias que sean pares")
reprobados_pares = notas[(notas <= 70) & (notas % 2 == 0)] #DEBE utilizar &
print(reprobados_pares)
print(SEPARADOR)

#Accesar datos específicos
print("La calificación de 'Pánfilo' en 'Programación'")
nota_PanfiloProgramacion = notas.at["Programación", "Pánfilo"]
print(nota_PanfiloProgramacion)
print(SEPARADOR)

#Modificar valores directamente
print("Modificaremos la nota de Pánfilo en programación")
notas.at["Programación", "Pánfilo"] = 80
nota_PanfiloProgramacion = notas.at["Programación", "Pánfilo"]
print(notas)