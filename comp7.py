#Un comercio ofrece un descuento del 15% sobre el total de la compra si esta supera los $1000. Obtenga para determinado 
#cliente cuánto deberá pagar finalmente por su compra y el descuento obtenido, si es que corresponde.


total_compra = float(input("Total de compra: $"))
descuento15 = total_compra * 0.15

if total_compra > 1000 :
    print (f"Total a pagar: $ {total_compra-descuento15}")
    print (f"El descuento aplicado es de : ${descuento15}")
else:
    print("no corresponden descuentos")

#resuelto
