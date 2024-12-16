"""
 Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista
excluyendo ciertas mascotas prohibidas en España. La lista de mascotas a excluir es ["Mapache", "Tigre",
"Serpiente Pitón", "Cocodrilo", "Oso"].Usa la función filter()
"""

def autorizator(animalType):
    banList = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]
    return (animalType not in banList)

listMascotas = ["Tigre", "Perro", "Oso", "Conejo", "Pulpo", "Cocodrilo", "Dragon Komodo"]

new_listMascotas = filter(autorizator, listMascotas)

for animal in new_listMascotas: print(animal)


# Aparentemente, se puede tener un dragon de Komodo como mascota ¯\_(ツ)_/¯
