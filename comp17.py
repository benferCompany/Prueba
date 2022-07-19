#Determinar y exhibir si la estatura de una persona adulta dada, es mayor que la estatura media de las personas adultas de su sexo, 
# siendo:

#- estatura media de mujeres adultas: 1,65 m.

#- estatura media de varones adultos: 1,72 m.


altura = float(input("Ingrese su altura: "))
sexo = input("Ingrese su sexo (M/H): ")

if sexo.upper() == "M" and altura > 1.65 :
    print("Usted tiene una altura mayor a la media para una mujer adulta.")
elif sexo.upper() == "H" and altura > 1.72 : 
    print("Usted tiene una altura mayor a la media para un hombre adulto.")
else :
    print("Usted tiene una altura media o menor a la media para su sexo")

#resuelto


