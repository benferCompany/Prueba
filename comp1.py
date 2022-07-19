#Solicite al usuario el ingreso de 3 números, e imprímalos de mayor a menor.

#OPCIONES
#numero 1 mayor a numero 2 y mayor a numero 3

numero1 = int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))
numero3 = int(input("Ingrese el tercer numero: "))

if numero2 < numero1 > numero3 and numero2 > numero3:
    print (numero1, numero2, numero3)
elif numero2 < numero1 > numero3 and numero2 < numero3:
    print (numero1, numero3, numero2)
elif numero1 < numero2 > numero3 and numero1 > numero3:
    print (numero2, numero1, numero3)
elif numero1 < numero2 > numero3 and numero1 < numero3:
    print (numero2, numero3, numero1)
elif numero1 < numero3 > numero2 and numero1 > numero2:
    print (numero3, numero1, numero2)
elif numero2 < numero3 > numero2 and numero1 < numero2:
    print (numero3, numero2, numero1)


#resuelto