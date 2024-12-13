"""
10. Escribe una función que reciba una lista de números y calcule su promedio. Si la lista está vacía, lanza una
excepción personalizada y maneja el error adecuadamente.
"""

def promedier(numList):

    try:
        promedio = sum(numList)/len(numList)
        return promedio

    except ZeroDivisionError:
        print("ERROR - There is a problem with the list, is it empty?")

listaNum = []
print(promedier(listaNum))