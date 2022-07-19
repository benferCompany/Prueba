#Un obrero necesita calcular su salario semanal, el cual se obtiene de la siguiente manera:

#i. Si trabaja 40 horas o menos se le paga $16 por hora

#ii. Si trabaja más de 40 horas se le paga $16 por cada una de las primeras 40 horas y $20 por cada hora extra.

horas_trabajo = int(input("Ingrese Horas Trabajadas: "))

if horas_trabajo <= 40:
    print(f"Salario Semanal : ${horas_trabajo*16}")
elif horas_trabajo > 40 :
    print (f"Salario Semanal: ${(40*16)+((horas_trabajo-40)*20)}")


#resuelto 


