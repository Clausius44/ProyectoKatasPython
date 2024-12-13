"""
22. Dada una lista numérica, obtén el producto total de los valores de dicha lista.Usa la función reduce() .
"""

from functools import reduce

def producter(num1, num2):

    return num1 * num2

numList = [2, 4, 5, 6, 10]

prod = reduce(producter, numList)
print(prod)