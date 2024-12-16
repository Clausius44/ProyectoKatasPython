"""
27.  Crea una función que calcule el promedio de una lista de números.
"""

def promedier(numList):

    return sum(numList)/len(numList)

numsToCheck = [2, 6, 5, 2, 6, 8, 12]
print(promedier(numsToCheck))
