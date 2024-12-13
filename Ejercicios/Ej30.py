"""
30. Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras
pero en diferente orden.
"""

def anagramizator(word1, word2):

    return (sorted(word1.lower()) == sorted(word2.lower()))

wordA = "casa"
wordB = "asac"

print(anagramizator(wordA, wordB))