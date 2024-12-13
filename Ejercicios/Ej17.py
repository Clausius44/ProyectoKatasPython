"""
17. Crea una función que tome una lista de dígitos y devuelva el número correspondiente. Por ejemplo, 5,7,2
corresponde al número quinientos setenta y dos 572. Usa la función reduce()
"""

from functools import reduce

def digiter(num1, num2):

    return str(num1) + str(num2)

listNums = [2, 5, 4, 4, 2, 4]

digits = reduce(digiter, listNums)
print(digits)