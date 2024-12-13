"""
19. Crea una función lambda que filtre los números impares de una lista dada.
"""

def onlyImpares(num):

    return (num%2 != 0)

numList = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

impares = list(filter(onlyImpares, numList))
print(impares)