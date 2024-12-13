"""
31. Crea una función que solicite al usuario ingresar una lista de nombres y luego solicite un nombre para buscar en
esa lista. Si el nombre está en la lista, se imprime un mensaje indicando que fue encontrado, de lo contrario, se
lanza una excepción.
"""

def pasarLista():

    nAlumnos = input("Que cantidad de alumnos vas a inscribir?\n----> ")

    try:
        nAlumnos = int(nAlumnos)
    except Exception as error:
        print("ERROR")
        print("No has introducido un valor aceptado")
        print("Introduce un valor entero y positivo")
        print("Saliendo del programa")
        quit()

    listaAlumnos = []
    for alumno in range(nAlumnos):
        nuevoAlumno = input("Introduce el nombre y apellido de un alumno\n----> ")
        listaAlumnos.append(nuevoAlumno)


    alumnoCheck = input("Introduce un nombre para comprobar si esta en la lista\n----> ")
    if alumnoCheck in listaAlumnos:
        print(f"El alumno {alumnoCheck} esta en la lista")
    else:
        print(f"El alumno {alumnoCheck} no esta en al lista")

lista = pasarLista()