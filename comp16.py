#Hacer un programa que calcule el total a pagar por la compra de camisas. Si se compran tres camisas o mas se aplica 
# un descuento del 20% sobre el total de la compra y si son menos de tres camisas un descuento del 10%.

precio_camisa = float(input("Ingrese Precio de unidad: $"))
cantidad = int(input("Ingrese cantidad de compra: "))
total_de_compra = precio_camisa * cantidad

descuento10 = total_de_compra * 0.1 
descuento20 = total_de_compra * 0.2


if cantidad>=3 :
    print(f"El monto total es: {total_de_compra }\nSe aplica descuento del 20%\nEl monto final es de: $ { total_de_compra - descuento20}")
else:
    print(f"El monto total es: {total_de_compra }\nSe aplica descuento del 10%\nEl monto final es de: $ { total_de_compra - descuento10}")


#resuelto