"""
18. Escribe un programa en Python que cree una lista de diccionarios que contenga información de estudiantes
(nombre, edad, calificación) y use la función filter para extraer a los estudiantes con una calificación mayor o igual a
90. Usa la función filter()
"""

def readStudent():

    name = input("Cual es el nombre del alunmo?\n----> ")
    age = input("Cual es la edad del alunmo?\n----> ")
    qualification = input("Cual es la calificación del alumno?\n----> ")

    student = {
        "name": name,
        "age": age,
        "qualification": float(qualification)
        }

    return student

def qualiSearch(student, num=90):

    return (student["qualification"] >= 90)

numAlum = int(input("Quantos alumnos quieres registrar?\n----> "))

listAlumns = []
for alum in range(numAlum):
    newAlum = readStudent()
    listAlumns.append(newAlum)

print("Vamos a revisar que alumnos tienen una calificación mayor o igual a 90:")

listaMayor = filter(qualiSearch, listAlumns)
print("Lista de alumnos que tienen una calificación mayor o igual que 90")
for alum in listaMayor:
    print(f"El alumno {alum["name"]} con una nota de {alum["qualification"]}")