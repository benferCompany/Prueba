#En un supermercado se hace una promoción, mediante la cual el cliente obtiene un descuento dependiendo de un número que se escoge al azar.
#  Si el numero escogido es menor que 74 el descuento es del 15% sobre el total de la compra, si es mayor o igual a 74 el descuento es 
# del 20%. Obtener cuánto dinero se le descuenta.

from random import randint

numero_aleatorio = randint(0,100)
total_compra = float(input("Ingrese total de compra : $"))
descuento15 = total_compra * 0.15 
descuento20 = total_compra * 0.20

print(f"El total de la compra es : ${total_compra}")
print(f"el numero sorteado es el : {numero_aleatorio}")

if numero_aleatorio < 74 : 
    print(f"El descuento correspondiente es de 15%\nEl precio final es de : ${total_compra - descuento15} ")
else :
    print(f"El descuento correspondiente es de 20%\nEl precio final es de : ${total_compra - descuento20} ")

print("GRACIAS POR SU COMPRA!")


#RESUELTO