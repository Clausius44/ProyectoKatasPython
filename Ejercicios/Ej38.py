"""
38. Genera un programa que nos diga si es de noche, de día o tarde según la hora proporcionada por el usuario.
"""

sunriseTime, sunsetTime = 7.50, 20.00

userTime = input("Sobre que hora quieres información (formato 24:00)?\n----> ")

workTime = userTime.split(":")
if workTime[1] != "00":
    workTime[0] = float(workTime[0]) + float(workTime[1])/60
    workTime = workTime[0]

else:
    workTime = float(workTime[0])

if workTime > sunriseTime and workTime < sunsetTime:
    print("Es de dia")
else:
    print("Es de noche")
