"""
13. Genera una función la cual, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en
mayúsculas y minúsculas. Las letras no pueden estar repetidas .Usa la función map()
"""

def function(letter):

    return (letter.upper(), letter.lower())

text = "aaahgDhibjnbefASfiuwubrgobeur"

listedLetters = list(set(map(function, [letter for letter in text])))

print(listedLetters)
