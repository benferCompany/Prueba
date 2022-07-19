#Hacer un programa que imprima el nombre de un artículo, clave, precio original y su precio con descuento. 
# El descuento lo hace en base a la clave, si la clave es 01 el descuento es del 10% y si la clave es 02 el descuento en 
# del 20% (solo existen dos claves).

Articulo = input("Nombre Articulo: ")
clave = input("Ingrese clave (01/02): ")
precio = float(input("Ingrese Precio: $"))

if clave == "01":
    print(f"{Articulo}\n{clave}\nprecio : ${precio}\nprecio c/descuento : ${precio * 1.1} ")
elif clave == "02":
    print(f"{Articulo}\n{clave}\nprecio : ${precio}\nprecio c/descuento : ${precio * 1.2} ")
else: 
    print("La clave ingresada en incorrecta")


#resuelta
