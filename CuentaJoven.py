"""

Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una persona) y cantidad (puede tener decimales). 

- El titular será obligatorio y la cantidad es opcional.  
- Implementa los siguientes métodos:

mostrar(): Muestra los datos de la cuenta.

ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa, no se hará nada.

retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos.






Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase CuantaJoven que deriva de lo que definas al resolver el problema Cuenta Electrónica. 

Cuando se crea esta nueva clase, además del titular y la cantidad se debe guardar una bonificación que estará expresada en tanto por ciento.Construye los siguientes métodos para la clase:

En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad, por lo tanto hay que crear un método esTitularValido() que devuelve verdadero si el titular es mayor de edad pero menor de 25 años y falso en caso contrario.

Además la retirada de dinero sólo se podrá hacer si el titular es válido.

El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de la cuenta.

Piensa los métodos heredados de la clase madre que hay que reescribir.
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

class cuentaJoven(Cuenta):
    def __init__(self, titular, edad, cantidad = 0, bonificacion = 0):
        super().__init__(titular, cantidad)
        self.bonificacion = bonificacion
        self.edad = edad
        
    def mostrar(self):
        if self.cantidad < 0:
            print(f'\033[0;31mTitular: {self.titular.capitalize()} | Edad: {self.edad} | Cantidad: {self.cantidad} | Bonificación: {self.bonificacion}% \033[0m')
        else:
            print(f'Titular: {self.titular.capitalize()} | Edad: {self.edad} | Cantidad: {self.cantidad} | Bonificación: {self.bonificacion}%')
    
    def esTitularValido(self):
        if self.edad > 17 and self.edad < 25:
            return True
        else:
            return False        

    def retirar(self, cantidad):
        if self.esTitularValido():
            self.cantidad -= cantidad
            print(f'Usted retiró ${cantidad}.')
            self.mostrar()
        else:
            print("Usuario no valido")


            
pedro = cuentaJoven("pedro", 26, 1800, 15)
pedro.mostrar()
pedro.retirar(230)