"""
23. Concatena una lista de palabras.Usa la función reduce() .
"""

from functools import reduce

def concater(string1, string2):

    return string1 + string2

stringList = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]
newString = str(reduce(concater, stringList))

print(newString)