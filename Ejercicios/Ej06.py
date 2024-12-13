"""
6. Escribe una función que calcule el factorial de un número de manera recursiva.
"""

def recursiver(num):

    if num == 1:
        return num
    return num * recursiver(num - 1)

numTest = 5
print(recursiver(numTest))
