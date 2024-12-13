"""
27. Crea una función lambda que calcule el resto de la división entre dos números dados.
"""

def promedier(numList):

    return sum(numList)/len(numList)

numsToCheck = [2, 6, 5, 2, 6, 8, 12]
print(promedier(numsToCheck))