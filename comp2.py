#Desarrolle un programa que permita determinar si un número X ingresado es par o impar.

numero = int(input("Ingrese un numero:\n"))

resto = numero % 2

if resto == 0 :
    print ("El numero es PAR")
else : 
    print("El numero es IMPAR")

#resuelto