"""
4. Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función map()
"""

def diferinator(list1, list2):

    if len(list1) > len(list2): print("La primera lista contiene mas elementos que la segunda")
    if len(list1) < len(list2): print("La segunda lista contiene mas elementos que la primera")

    answerList = []
    for num1, num2 in zip(list1, list2):
        answerList.append(num1 - num2)

    return answerList

testLista1 = [2, 4, 5, 2, 7, 9, 12]
testLista2 = [3, 5, 7, 2, 1, 8]

print(diferinator(testLista2, testLista1))