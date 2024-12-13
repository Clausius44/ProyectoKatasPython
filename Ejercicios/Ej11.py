"""
11. Escribe un programa que pida al usuario que introduzca su edad. Si el usuario ingresa un valor no numérico o un
valor fuera del rango esperado (por ejemplo, menor que 0 o mayor que 120, maneja las excepciones
adecuadamente.
"""
# No he añadido un error por si la edad esta fuera de rango, lo he lidiado con un if en el caso de que la edad sea un
# numero valido

print("Please give me your age:")
userAge = input("What is your are?\n----> ")

ageMin, ageMax = 0, 120
try:
    userAge = int(userAge)
    if userAge < ageMin or userAge > ageMax:
        print(f"ERROR - The age must be in the range of {ageMin} to {ageMax}")
    
except ValueError:
    print("ERROR - The age must be a number")
    exit()
