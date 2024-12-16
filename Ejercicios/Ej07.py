"""
7. Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map()
"""

def converter(thing):

    return str(thing)

lisTupla = [("casa"), ("coche"), ("pajaro"), ("armadillo")]
newLista = map(converter, lisTupla)

for thing in newLista:
    print(thing)
