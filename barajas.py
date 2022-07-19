"""

Vamos a hacer una baraja de cartas españolas orientado a objetos.

Una carta tiene un número entre 1 y 12 (el 8 y el 9 no los incluimos) y un palo (espadas, bastos, oros y copas)

La baraja estará compuesta por un conjunto de cartas, 40 exactamente.

Las operaciones que podrá realizar la baraja son:

barajar: cambia de posición todas las cartas aleatoriamente

cartasDisponibles: indica el número de cartas que aún puede repartir

darCartas: dado un número de cartas que nos pidan, le devolveremos ese número de cartas (piensa que puedes devolver). En caso de que haya menos cartas que las pedidas, no devolveremos nada pero debemos indicárselo al usuario.

cartasMonton: mostramos aquellas cartas que ya han salido, si no ha salido ninguna indicárselo al usuario

mostrarBaraja: muestra todas las cartas hasta el final. Es decir, si se saca una carta y luego se llama al método, este no mostrara esa primera carta.

siguienteCarta: devuelve la siguiente carta que está en la baraja, cuando no haya más o se haya llegado al final, se indica al usuario que no hay más cartas.

"""
from random import shuffle
from os import system
from time import sleep

system('cls')

prefijo = "\033["
reestablecer = f"{prefijo}0m"

class colores:
    claro_off = "0;"
    claro_on = "1;"
    negro = "30m"
    rojo = "31m"
    verde = "32m"
    amarillo = "33m"
    azul = "34m"
    violeta = "35m"
    celeste = "36m"
    blanco = "37m"

    black="\033[0;30m"
    red="\033[0;31m"
    green="\033[0;32m"
    brown="\033[0;33m"
    blue="\033[0;34m"
    purple="\033[0;35m"
    cyan="\033[0;36m"
    light_gray="\033[0;37m"
    dark_gray="\033[1;30m"
    light_red="\033[1;31m "
    light_green="\033[1;32m"
    amarillo="\033[1;33m"
    light_blue="\033[1;34m"
    light_purple="\033[1;35m"
    light_cyan="\033[1;36m"
    light_white="\033[1;37m"

    bold="\033[1m"
    faint="\033[2m"
    italic="\033[3m"
    underline="\033[4m"
    blink="\033[5m"
    negative="\033[7m"
    crossed="\033[9m"

def fuente(texto, color=colores.blanco, negrita=False, subrayado=False):
    return f'{prefijo}{("1;" if negrita else "") + ("4;" if subrayado else "")}{color}{texto}{reestablecer}'

def fuente2(texto, color=colores.blanco, negrita=False, subrayado=False, claro=False):
    return f'{colores.bold if negrita else ""}{colores.underline if subrayado else ""}{prefijo}{colores.claro_on if claro else colores.claro_off}{color}{texto}{reestablecer}'

def mensaje(titulo, contenido, color = colores.blanco, tiempo = 2.0, desfase = 61):
    system('cls')
    print(f' {fuente(titulo, color, True, False)} '.center(desfase, '*'))
    print(fuente(contenido, color, True, False).center(61, ' '))
    print('*********'.center(50, '*'))
    sleep(tiempo)

class Carta:
    def __init__(self, numero, palo):
        self.numero = numero
        self.palo = palo

    def __repr__(self):
      return f'{self.numero} {self.palo}'


class Baraja:
    def __init__(self):
        self.cartas = []
        self.cartas_descartadas = []
        self.barajar()

    def crearCartas(self):
        self.cartas = []
        self.cartas_descartadas = []
        for palo in ['de Espadas', 'de Basto', 'de Copas', 'de Oro']:
            for numero in range(1, 13):
                if numero != 8 and numero != 9:
                    carta = Carta(numero, palo)
                    self.cartas.append(carta)

    def barajar(self):
        self.crearCartas()
        shuffle(self.cartas)
        mensaje(' 🃏 HECHO 🃏 ', 'Cartas del mazo mezcladas.', colores.verde, 2, 58)

    def cartasDisponibles(self):
        system('cls')
        if len(self.cartas) > 0:
          print('********************************')
          print(' ')
          print(f"Quedan {len(self.cartas)} cartas en el mazo.")
          print(' ')
          print('********************************')
          input()
        else: mensaje(' ERROR ', 'No hay más cartas en el mazo.', colores.rojo)

    def darCartas(self, cantidad):
        system('cls')
        cartas_a_dar = []
        if cantidad <= len(self.cartas):
          print('********************************')
          print(' ')
          print('DISTE LAS CARTAS:')
          for carta in range(cantidad):
            carta_sacada = self.cartas.pop()
            print(carta_sacada)
            self.cartas_descartadas.append(carta_sacada) 
            cartas_a_dar.append(carta_sacada)
          print(' ')
          print('********************************')
          input()
        else: mensaje(' ERROR ', 'No tenemos tantas cartas en el mazo.', colores.rojo)
        return cartas_a_dar

    def siguienteCarta(self):
        system('cls')
        if len(self.cartas) > 0:
          print('********************************')
          print(' ')
          print('LA SIGUIENTE CARTA ES: ')
          print(self.cartas[-1])
          print(' ')
          print('********************************')
          input()
        else: mensaje(' ERROR ', 'No hay más cartas en el mazo.', colores.rojo)

    def mostrarBaraja(self):
        system('cls')
        print('********************************')
        print(' ')
        print(f'CARTAS EN EL MAZO ({len(self.cartas)}):')
        if len(self.cartas) > 0:
            for carta in self.cartas:
                print(carta)
            print(' ')
            print('********************************')
            input()
        else: mensaje(' ERROR ', 'No hay más cartas en el mazo.', colores.rojo)
        
      
    def cartasMonton(self):
        system('cls')
        print('********************************')
        print(' ')
        print(f'CARTAS QUE YA HAN SALIDO ({len(self.cartas_descartadas)}):')
        if len(self.cartas_descartadas) > 0:
            for carta in self.cartas_descartadas:
                print(carta)
            print(' ')
            print('********************************')
            input()
        else: mensaje(' ERROR ', 'No sacaste cartas aún.', colores.rojo)

baraja = Baraja()

def menu():
  system('cls')
  print(' MENU '.center(32, '*'))
  print(' ')
  print('1. Dar cartas')
  print('2. Número de cartas disponibles')
  print('3. Mostrar siguiente carta')
  print('4. Mostrar cartas en el mazo')
  print('5. Mostrar cartas descartadas')
  print('6. Barajar de nuevo')
  print('7. SALIR')
  print(' ')
  print('********************************')

while True:
  menu()
  try:
    opcion = int(input('Elegir: '))
    if opcion == 1:
      cantidad = int(input('¿Cuántas cartas va a dar?: '))
      baraja.darCartas(cantidad)
    elif opcion == 2:
      baraja.cartasDisponibles()
    elif opcion == 3:
      baraja.siguienteCarta()
    elif opcion == 4:
      baraja.mostrarBaraja()
    elif opcion == 5:
      baraja.cartasMonton()
    elif opcion == 6:
      baraja.barajar()
    elif opcion == 7:
      system('cls')
      mensaje(' 🏃 FIN DEL PROGRAMA 🏃 ', 'Gracias por usar nuestro programa.', colores.rojo)
      sleep(3)
      system('cls')
      break
    else:
      mensaje(' ERROR ','Solo se admite opciones del 1-7.', colores.rojo)
  except ValueError:
    mensaje(' ERROR ', 'Solo se admiten valores númericos', colores.rojo)
