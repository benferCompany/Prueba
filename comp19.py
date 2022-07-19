# Una distribuidora de libros vende a librerías y a particulares. 
# Aplica bonificaciones por cantidad según el siguiente criterio:

#i.a librerías: hasta 24 unidades, el 20%; más de 24 unidades, el 25%.
#ii. a particulares: menos de 6 unidades, nada; desde 6 hasta 18 unidades, el 5% y más de 18 unidades, el 10%.
#El tipo de cliente está codificado así: 'L' para librerías, 'P' para particular. 
# Dado el importe bruto de una compra de libros, el tipo de cliente de que se trata y la cantidad total pedida por el mismo,
# determinar el importe bruto bonificado.

precio_unidad = float(input("Ingrese precio de unidad: $"))
tipo_cliente = input("Ingrese tipo cliente (P/L): ")
cantidad_unidades = int(input("Ingrese cantidad de unidades: "))
importe_bruto = precio_unidad * cantidad_unidades

descuento25 = importe_bruto - (importe_bruto * 0.25)
descuento20 = importe_bruto - (importe_bruto * 0.20)
descuento10 = importe_bruto - (importe_bruto * 0.10)
descuento5 = importe_bruto - (importe_bruto * 0.05)

if tipo_cliente.upper() == "L" and cantidad_unidades <= 24:
    print(f"el importe bruto es de : ${importe_bruto}")
    print("Corresponde un descuento de 20%")
    print(f"el importe final es de : ${descuento20}")
elif tipo_cliente.upper() == "L" and cantidad_unidades > 24:
    print(f"el importe bruto es de : ${importe_bruto}")
    print("Corresponde un descuento de 25%")
    print(f"el importe final es de : ${descuento25}")
elif tipo_cliente.upper() == "P" and 6 <= cantidad_unidades <= 18:
    print(f"el importe bruto es de : ${importe_bruto}")
    print("Corresponde un descuento de 5%")
    print(f"el importe final es de : ${descuento5}")
elif tipo_cliente.upper() == "P" and cantidad_unidades > 18:
    print(f"el importe bruto es de : ${importe_bruto}")
    print("Corresponde un descuento de 10%")
    print(f"el importe final es de : ${descuento10}")
else:
    print(f"el importe bruto es de : ${importe_bruto}")
    print("No corresponde un descuento ")

#resuelto




