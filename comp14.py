#Leer 2 números; si son iguales que los multiplique, si el primero es mayor que el segundo que los reste y si no que los sume.

numero1 = float(input("Ingrese Numero 1: "))
numero2 = float(input("Ingrese Numero 2: "))

if numero1 == numero2 :
    print(f"{numero1 * numero2}")
elif numero1 > numero2 :
    print(f"{numero1 - numero2}")
else:
    print(f"{numero1 + numero2} ")


# resuelto