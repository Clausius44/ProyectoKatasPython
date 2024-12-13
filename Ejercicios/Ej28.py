"""
28. Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.
"""

def duplicator(lista):

    memory = []

    for thing in lista:
        if thing not in memory:
            memory.append(thing)
        elif thing in memory:
            return thing

listToCheck = [1, 4, 2, 4, 6, 7, 1, 2, 7]
print(duplicator(listToCheck))