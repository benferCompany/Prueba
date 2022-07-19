#Diseñar un programa que lea las longitudes de los tres lados de un triángulo (L1,L2,L3) y determine qué 
# tipo de triángulo es, de acuerdo a los siguientes casos. Suponiendo que A determina el mayor de los tres lados y B y C 
# corresponden con los otros dos, entonces:

#Si A>=B + C à No se trata de un triángulo

#Si A2 = B2 + C2 à Es un triángulo rectángulo

#Si A2 > B2 + C2 à Es un triángulo obtusángulo

#Si A2 < B2 + C2 à Es un triángulo acutángulo

A = float(input("Ingrese longitud de lado 1 (mayor): "))
B = float(input("Ingrese longitud de lado 2: "))
C = float(input("Ingrese longitud de lado 3: "))

A2 = A*A
B2 = B*B
C2 = C*C


if A >= (B+C):
    print("Las dimenciones dadas no corresponden a un triangulo")
elif A2 == (B2 + C2 ):
    print("Las dimenciones dadas corresponden a un triangulo RECTANGULO")
elif A2 > ( B2 + C2):
    print("Las dimenciones dadas corresponden a un triangulo OBTUSANGULO")
elif A2 < ( B2 + C2):
    print("Las dimenciones dadas corresponden a un triangulo ACUTANGULO")

#RESUELTO
