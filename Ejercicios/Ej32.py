"""
32. Crea una función que tome un nombre completo y una lista de empleados, busque el nombre completo en la lista y
devuelve el puesto del empleado si está en la lista, de lo contrario, devuelve un mensaje indicando que la persona
no trabaja aquí.
"""

def comprobadorEmpleo(empleado, lista):

    if empleado in lista.keys():
        return lista[empleado]
    else:
        print(f"{empleado} no esta registrado como trabajador")

dictEmpleados = {
    "Pepe": "gerente",
    "Paco": "conserge",
    "Pol": "obrero"
    }

print(comprobadorEmpleo("Paco", dictEmpleados))