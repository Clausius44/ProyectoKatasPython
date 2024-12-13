"""
37. Crea una función llamada procesar_texto que procesa un texto según la opción especificada: contar_palabras ,
reemplazar_palabras , eliminar_palabra . Estas opciones son otras funciones que tenemos que definir primero y llamar dentro
de la función procesar_texto .
"""

def procesar_texto(text, mode, *args):

    if mode == "contar_palabras":
        return len(text.split())

    if mode == "reemplazar_palabra":
        palabra_original = args[0]
        palabra_nueva = args[1]
        text = text.replace(palabra_original, palabra_nueva)
        return text

    if mode == "eliminar_palabra":
        palabra_eliminar = args[0]
        text = text.replace(palabra_eliminar, "")
        return text

texto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

print(procesar_texto(texto, "contar_palabras"))
print(procesar_texto(texto, "reemplazar_palabra", "ipsum", "apio"))
print(procesar_texto(texto, "eliminar_palabra", "aliqua"))