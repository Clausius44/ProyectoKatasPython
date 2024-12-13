"""
41. En este ejercicio, se te pedirá que escribas un programa en Python que utilice condicionales para determinar el
monto final de una compra en una tienda en línea, después de aplicar un descuento.
"""

precioFinal = float(input("Cual es la cantidad final de su compra?\n----> "))
cupon = input("Posee un cupon de descuento (Si/No)?\n----> ")

if cupon == "Si":
    cupon = True
    descuento = float(input("De que cantidad es el cupon de descuento?\n----> "))
    precioFinal -= descuento
elif cupon == "No":
    cupon = False
else:
    print("No se ha podido procesar, se asumira que no dispone de cupon")

print(f"La cantidad total final es de {precioFinal:.2f} €")
print("Gracias por su visita")