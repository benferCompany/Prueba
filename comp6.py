#Un equipo de fútbol ha tenido una buena campaña y desea premiar a sus jugadores con un aumento del salario para la siguiente campaña. 
# Los sueldos deben ajustarse de la siguiente forma:

#Sueldo Actual (en $)           Aumento
#0 – 6000							15%
#6000 – 7900					   10%
#7900 – 12000			     		6%
#Más de 12000				         0%
#Diseñar un programa que lea el salario de un jugador, y que a continuación muestre el tanto por ciento de aumento, 
# el sueldo actual y el sueldo aumentado.


sueldo_actual = float(input("Ingrese el sueldo actual : $"))
aumento_15 = sueldo_actual * 1.15
aumento_10 = sueldo_actual * 1.10
aumento_6 = sueldo_actual * 1.06
aumento_0 = sueldo_actual

if sueldo_actual <= 6000 :
    print(f"El aunmento correspondiente es de 15%,\nEl sueldo actual es de ${sueldo_actual}\nEl sueldo aumentado es de ${aumento_15}")
elif 6000 < sueldo_actual < 7900:
    print(f"El aunmento correspondiente es de 10%,\nEl sueldo actual es de ${sueldo_actual}\nEl sueldo aumentado es de ${aumento_10}")
elif 7900 < sueldo_actual <= 12000 :
    print(f"El aunmento correspondiente es de 6%,\nEl sueldo actual es de ${sueldo_actual}\nEl sueldo aumentado es de ${aumento_6}")
elif sueldo_actual > 12000 :
    print("No corresponde aumento de sueldo")


