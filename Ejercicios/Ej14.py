"""
14. Crea una función que retorne las palabras de una lista de palabras que comience con una letra en especifico. Usa la
función filter()
"""

def selector(word):

    return (word[0].lower() == letter.lower())

wordList = ["alfa", "becerro", "puerro", "banco", "zozobrar", "bocina"]

global letter
letter = "b"
new_wordList = filter(selector, wordList)

for word in new_wordList: print(word)
