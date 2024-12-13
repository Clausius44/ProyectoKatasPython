"""
12. Genera una función que al recibir una frase devuelva una lista con la longitud de cada palabra. Usa la función map()
"""

def longitudPalabra(word):

    workWord = word.replace(".", "").replace(",", "")
    return len(workWord)

texto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

vecLongitudes = list(map(longitudPalabra, texto.split()))
for word, len in zip(texto.split(), vecLongitudes):
    print(word, len)