#Realizar un programa que sea capaz de, habiéndose ingresado dos números m y n, determine si n es divisor de m.

numero1 = float(input("Ingrese numero 1: "))
numero2 = float(input("Ingrese numero 2: "))

resto = numero1 % numero2

if resto == 0 :
    print(f"El numero {numero2} ingresado SI es divisor {numero1}")
else:
    print(f"El numero {numero2} ingresado NO es divisor {numero1}")


#RESUELTO