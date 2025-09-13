#1)
edad=int(input("Ingrese su edad: "))
if edad>18:
    print("Es mayor de edad.")

#2)
nota=int(input("Ingrese su nota: "))
if nota>=6:
    print("Aprobado")
else:
    print("Desaprobado")

#3)
num=int(input("Ingrese un numero "))
if num % 2 == 0:
    print("Ha ingresado un numero par.")
else:
    print("Por favor, infrece un numero par.")

#4)
edad=int(input("Ingrese su edad: "))
if edad<12:
    print("Niño")
elif edad >=12 and edad<18:
    print("Adolescente")
elif edad >=18 and edad<30:
    print("Adulto/a joven")
elif edad >= 30:
    print("Adulto/a")

#5)
passw=input("Ingrese una contraseña: ")
if len(passw) >= 8 and len(passw)<=14:
    print("Ha ingresado una contraseña correcta.")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#6)
from statistics import mode, median, mean
import random
numeros_aleatorios=[random.radint(1,100) for i in range[50]]
moda=mode(numeros_aleatorios)
media=mean(numeros_aleatorios)
mediana=median(numeros_aleatorios)
if media>mediana>moda:
    print("Sesgo positivo o a la derecha.")
elif media<mediana<moda:
    print("Sesgo negativo o a la izquierda")
elif media==mediana==moda:
    print("Sin sesgo")

#7)
vocales=["a","e","i","o","u"]
frase=input("Ingrese una frase o palabra: ").lower()
if frase[-1] in vocales:
    print(f"{frase}!")
else:
    print(frase)

#8)
nombre=input("Ingrese su nombre: ")
while True:
    opcion=input("""Ingrese una opcion:
1:Tu nombre en mayusculas
2:Tu nombre en minusculas
3:La primer letra en mayusculas
""")
    if opcion=="1":
        print(nombre.upper())
        break
    elif opcion=="2":
        print(nombre.lower())
        break
    elif opcion=="3":
        print(nombre.title())
        break
    else:
        print("Opcion incorrecta.")

#9)
mag=int(input("Ingrees la magnitud del terremoto: "))
if mag<3:
    print("Muy leve")
elif mag>=3 & mag<4:
    print("Leve")
elif mag>4 & mag<5:
    print("Moderado")
elif mag>5 & mag<6:
    print("Fuerte")
elif mag>6 & mag<7:
    print("Muy fuerte")
else:
    print("Extremo")

#10)
hemisferio = input("En qué hemisferio te encuentras? (N/S): ")
mes = input("Que mes es?: ").lower()
dia = int(input("Que dia es?: "))

meses = {
    "enero": 1, "febrero": 2, "marzo": 3, "abril": 4,
    "mayo": 5, "junio": 6, "julio": 7, "agosto": 8,
    "septiembre": 9, "octubre": 10, "noviembre": 11, "diciembre": 12
}

mes = meses[mes]

if hemisferio.upper() == "N": 
    if (mes == 12 and dia >= 21) or (1 <= mes <= 2) or (mes == 3 and dia <= 20):
        estacion = "Invierno"
    elif (mes == 3 and dia >= 21) or (4 <= mes <= 5) or (mes == 6 and dia <= 20):
        estacion = "Primavera"
    elif (mes == 6 and dia >= 21) or (7 <= mes <= 8) or (mes == 9 and dia <= 20):
        estacion = "Verano"
    else:
        estacion = "Otoño"

elif hemisferio.upper() == "S":
    if (mes == 12 and dia >= 21) or (1 <= mes <= 2) or (mes == 3 and dia <= 20):
        estacion = "Verano"
    elif (mes == 3 and dia >= 21) or (4 <= mes <= 5) or (mes == 6 and dia <= 20):
        estacion = "Otoño"
    elif (mes == 6 and dia >= 21) or (7 <= mes <= 8) or (mes == 9 and dia <= 20):
        estacion = "Invierno"
    else:
        estacion = "Primavera"

print("La estacion es:", estacion)
