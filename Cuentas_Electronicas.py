"""
Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una persona) y cantidad (puede tener decimales). 
- El titular será obligatorio y la cantidad es opcional.  
- Implementa los siguientes métodos:

mostrar(): Muestra los datos de la cuenta.
ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa, no se hará nada.
retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos.

"""
class Cuenta:
    def __init__(self, titular, cantidad = 0) -> None:
        self.titular = titular
        self.cantidad = cantidad

    def mostrar(self):
        if self.cantidad < 0:
            print(f'\033[0;31mTitular: {self.titular} | Cantidad: {self.cantidad} \033[0m')
        else:
            print(f'Titular: {self.titular} | Cantidad: {self.cantidad}')

    def ingresar(self, cantidad):
        if cantidad > 0:
            self.cantidad += cantidad

    def retirar(self, cantidad):
        self.cantidad -= cantidad

juan = Cuenta('Juan')
juan.mostrar()

juan.ingresar(100)
juan.mostrar()

juan.retirar(5000)
juan.mostrar()