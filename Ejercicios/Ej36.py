"""
36. Crea la clase UsuarioBanco ,representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta
corriente. Proporciona métodos para realizar operaciones como retirar dinero, transferir dinero desde otro usuario y
agregar dinero al saldo
"""

class usuarioBanco():

    def __init__(self, nombre, saldo, cuenta):
        self.nombre = nombre
        self.saldo = saldo
        self.cuenta = cuenta

    def retirar_dinero(self, cantidad):
        if cantidad > self.saldo:
            print("No se puede retirar esa cantidada, no hay suficiente saldo suficiente")
        else:
            self.saldo -= cantidad

    def transferir_dinero(self, cantidad, destinatario):
        if cantidad > self.saldo:
            print("No se puede transferir esa cantidada, no hay suficiente saldo suficiente")
        else:
            self.saldo -= cantidad
            destinatario.saldo += cantidad

    def agregar_dinero(self, cantidad):
        self.saldo += cantidad

Alice = usuarioBanco("Alice", 100, True)
Bob = usuarioBanco("Bob", 50, True)
Bob.agregar_dinero(20)
Bob.transferir_dinero(80, Alice)
Alice.retirar_dinero(50)

print(Alice.saldo)
print(Bob.saldo)
