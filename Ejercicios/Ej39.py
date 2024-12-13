"""
39. Escribe un programa que determine qué calificación en texto tiene un alumno en base a su calificación numérica.
"""

notaAlumno = input("Que nota quiere evaluar (de 0 a 100)?\n----> ")
notaAlumno = int(notaAlumno)

if notaAlumno < 70:
    print("Insuficiente")
if notaAlumno > 69 and notaAlumno < 80:
    print("Bien")
if notaAlumno > 79 and notaAlumno < 90:
    print("Muy bien")
if notaAlumno > 89:
    print("Excelente")
