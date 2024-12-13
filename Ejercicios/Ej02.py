"""
2. Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map()
"""

def squarer(x):
    return x**2

numList = [2, 4, 6, 8, 3, 4, 6, 4, 1, 9, 2, 7, 8, 4]

new_numList = list(map(squarer, numList))
print(new_numList)