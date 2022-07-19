#Determinar si un alumno aprueba a reprueba un curso, sabiendo que aprobara si su promedio de tres calificaciones 
# es mayor o igual a 70; desaprueba en caso contrario.

calificacion1 = int(input("Ingrese calificacion 1 (0 al 100): "))
calificacion2 = int(input("Ingrese calificacion 2 (0 al 100): "))
calificacion3 = int(input("Ingrese calificacion 3 (0 al 100): "))

promedio_calificacion = (calificacion1 + calificacion2 + calificacion3)/3

if promedio_calificacion >= 70:
    print(f"Promedio : {int(promedio_calificacion)}")
    print("Alumno APROBADO")
else:
    print(f"Promedio : {int(promedio_calificacion)}")
    print("Alumno DESAPROBADO")

