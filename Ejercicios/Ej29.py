"""
29. Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres con el
carácter '#', excepto los últimos cuatro.
"""

def depuratorHastag(text):

    hashCount = 4
    new_text = ""

    for letter in text:
        if letter == "#" and hashCount > 0:
            hashCount -= 1
            continue

        if hashCount < 1:
            new_text = new_text + letter
            continue

        else:
            new_text = new_text + letter

    return new_text

sampleText = "asjfsjeg###asjfjsrg##esjgaonegr#######"
print(depuratorHastag(sampleText))