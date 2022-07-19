#Se leen tres números que son las longitudes de los lados de un triángulo. Determinar e informar si el mismo es equilátero 
# (3 lados iguales), isósceles (2 lados iguales) o escaleno (3 lados distintos).

lado1 = float(input("Ingrese longitud Lado 1 : "))
lado2 = float(input("Ingrese longitud Lado 2 : "))
lado3 = float(input("Ingrese longitud Lado 3 : "))


if lado1 == lado2 ==lado3 :
    print("El triangulo es un EQUILATERO")
elif lado1 == lado2 and lado1 != lado3 :
    print("El triangulo es un ISOSCELES")
elif lado1 == lado3 and lado1 != lado2 :
    print("El triangulo es un ISOSCELES")
elif lado2 == lado3 and lado2 != lado1 :
    print("El triangulo es un ISOSCELES")
elif lado1 != lado2 != lado3:
     print("El triangulo es un ESCALENO")

#RESUELTO