"""
8. Escribe un programa que pida al usuario dos números e intente dividirlos. Si el usuario ingresa un valor no numérico
o intenta dividir por cero, maneja esas excepciones de manera adecuada. Asegúrate de mostrar un mensaje
indicando si la división fue exitosa o no.
"""

print("This program divide two numbres if possible")
print()
print("Give me the first numbere to divide")
num1 = input("First number\n---->  ")
print()
print("Give me the second numbre to divide")
num2 = input("Second number\n---->  ")

print("The chosen numbers are {} and {}".format(num1, num2))
print()

try:
    num1, num2 = float(num1), float(num2)
    result = num1/num2
    print("Successful division!")
    print("The result is {}".format(result))

except ValueError:
    print("ERROR - one of the inputs is not a number")

except ZeroDivisionError:
    print("ERROR - you just tried to divide by zero")
