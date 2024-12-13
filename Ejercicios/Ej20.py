"""
20.  Para una lista con elementos tipo integer y string obtén una nueva lista sólo con los valores int. Usa la función
filter()
"""

def filtro(thing):

    return (type(thing) == int)

checkList = [4, "cosa", 2, 5, "otra_cosa", 12, "ultima_cosa"]

integers = list(filter(filtro, checkList))
print(integers)