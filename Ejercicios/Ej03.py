"""
3. Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. La función debe
devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo.
"""

def searcher(wordList, word):

    answer = []
    for thing in wordList:
        if word in thing:
            answer.append(thing)

    return answer

testList = ["casa", "casamiento", "encarar", "costilla", "trueno", "acabar", "castillo"]
toSearch = "casa"

print(searcher(testList, toSearch))