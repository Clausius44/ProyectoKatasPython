"""
40. Escribe una función que tome dos parámetros: figura (una cadena que puede ser "rectangulo" , "circulo" o
"triangulo" ) y datos (una tupla con los datos necesarios para calcular el área de la figura).
"""

def calculoGeometrico(figura, datos):

    area = "Figura no reconocida"

    if figura == "rectangulo":
        area = datos[0] * datos[1]
    if figura == "triangulo":
        area = (datos[0] * datos[1])/2
    if figura == "circulo":
        area = 3.1415926 * datos[0]**2

    return area

print(calculoGeometrico("rectangulo", (4, 7)))
print(calculoGeometrico("triangulo", (4, 7)))
print(calculoGeometrico("circulo", (4, )))
print(calculoGeometrico("trapezio", 4))
