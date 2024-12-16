"""
4. Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función map()
"""

def diference(num1, num2):

    return num1 - num2

testLista1 = [2, 4, 5, 2, 7, 9, 12]
testLista2 = [3, 5, 7, 2, 1, 8]

difList = list(map(diference, testLista1, testLista2))

print(difList)
