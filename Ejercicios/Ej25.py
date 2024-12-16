"""
25. Crea una función que cuente el número de caracteres en una cadena de texto dada.
"""
# Seria mas optimo utilizar un len(texto), pero he pensado que utilizar el bucle for con el operador += era lo que habia de demostrar ya que el enunciado pide
# que la función "cuente el numero de caracteres".

def charCount(string):
    total = 0
    for char in string:
        total += 1
    return total

texto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

totalChar = charCount(texto)
print(totalChar)
