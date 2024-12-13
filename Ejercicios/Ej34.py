"""
34. Crea la clase Arbol , define un árbol genérico con un tronco y ramas como atributos. Los métodos disponibles son:
crecer_tronco , nueva_rama , crecer_ramas , quitar_rama e info_arbol . El objetivo es implementar estos métodos para
manipular la estructura del árbol.
"""

class Arbol():

    def __init__(self):
        self.tronco = 1
        self.ramas = []

    def crecer_tronco(self):
        self.tronco += 1

    def nueva_rama(self):
        self.ramas.append(1)

    def crecer_ramas(self):
        for rama, longitud in enumerate(self.ramas):
            self.ramas[rama] += 1

    def quitar_rama(self, num):
        self.ramas.pop(num)

    def info_arbol(self):
        print(f"Longitud del tronco -> {self.tronco}")
        if len(self.ramas) == 0:
            print("No hay ramas")
        else:
            for rama, longitud in enumerate(self.ramas):
                print(f"Rama {rama} con longitud {longitud}")

arbol = Arbol()
arbol.crecer_tronco()
arbol.nueva_rama()
arbol.crecer_ramas()
arbol.nueva_rama()
arbol.nueva_rama()
arbol.quitar_rama(2)
arbol.info_arbol()
