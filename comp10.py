#Tres personas deciden invertir su dinero para fundar una empresa. Cada una de ellas invierte una cantidad distinta.
# Obtener el porcentaje que cada quien invierte con respecto a la 
# cantidad total invertida.

inversor1 = float(input("Inversor 1 : $"))
inversor2 = float(input("Inversor 2 : $"))
inversor3 = float(input("Inversor 3 : $"))

total_inversion = inversor1 + inversor2 + inversor3

print(f"CANTIDAD TOTAL : ${total_inversion}")
print(f"Porcentaje Inversor 1 : %{inversor1 * 100 / total_inversion}")
print(f"Porcentaje Inversor 2 : %{inversor2 * 100 / total_inversion}")
print(f"Porcentaje Inversor 3 : %{inversor3 * 100 / total_inversion}")


#ver forma de limitar decimales
#resuelto