"""
5. Ecribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado, que por
defecto es 5. La función debe calcular la media de los números en la lista y determinar si la media es mayor o igual
que nota aprobado. Si es así, el estado será "aprobado", de lo contrario, será "suspenso". La función debe devolver
una tupla que contenga la media y el estado.
"""

def evaluator(listNotas, notaAprobado = 5):

    evaluacion = "Aprobado"
    promedio = 0
    for nota in listNotas:
        promedio += nota
    promedio = promedio/len(listNotas)
    if promedio < notaAprobado: evaluacion = "Suspenso"

    return (promedio, evaluacion)

notasAlumno = [4, 5, 5.6, 9.2, 2, 7]

print(evaluator(notasAlumno))