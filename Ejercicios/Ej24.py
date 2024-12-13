"""
24. Calcula la diferencia total en los valores de una lista. Usa la función reduce() .
"""

from functools import reduce

def diference(num1, num2):

    return num1 - num2

numList = [2, 4, 5, 6, 10]

dife = reduce(diference, numList)
print(dife)