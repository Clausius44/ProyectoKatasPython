"""
1. Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias
de cada letra en la cadena. Los espacios no deben ser considerados.
"""

def freqFinder(text):
    dictFreq = {}
    avoid = [" ", ",", "."]

    for letter in text:
        workLetter = letter.lower()
        if workLetter in avoid:
            continue

        if workLetter not in dictFreq.keys():
            dictFreq[workLetter] = 1

        else:
            dictFreq[workLetter] += 1

    return dictFreq

texto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

dictoFreq = freqFinder(texto)

for letter, freq in dictoFreq.items():
    print(letter, freq)
