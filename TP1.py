#1)
print(f"Hola mundo!")

#2)
nombre=input("Indica tu nombre: ")
print(f"Hola {nombre}!")

#3)
nombre=input("Indica tu nombre: ")
apellido=input("Indica tu apellido: ")
edad=input("Indica tu edad: ")
residencia=input("Indica tu residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

#4)
radio=float(input("Ingrese el radio de un circulo"))
area=3.14*radio*radio
print(f"El area del circulo es: {area}")

#5)
seg=int(input("Ingrese una cantidad de segundos: "))
horas=seg/60/60
print(f"{seg} segundos son {horas} horas.")

#6)
num=float(input("Ingrese un numero: "))
print(f"{num} * 1 = {num*1} " )
print(f"{num} * 2 = {num*2} " )
print(f"{num} * 3 = {num*3} " )
print(f"{num} * 4 = {num*4} " )
print(f"{num} * 5 = {num*5} " )
print(f"{num} * 6 = {num*6} " )
print(f"{num} * 7 = {num*7} " )
print(f"{num} * 8 = {num*8} " )
print(f"{num} * 9 = {num*9} " )
print(f"{num} * 10 = {num*10} " )

#7)
num1=float(input("Ingrese dos numeros: "))
num2=float(input())
print(f"Suma: {num1+num2}")
print(f"Resta: {num1-num2}")
print(f"Multiplicacion: {num1*num2}")
print(f"Division: {num1/num2}")

#8)
peso=float(input("Ingrese su peso: "))
altura=float(input("Ingrese su altura en metros"))
print(f"Su IMC es: {peso/(altura*altura)}")

#9) 
temp_c=float(input("Ingrese la temperatura en grados Celcius: "))
print(f"La temperatura en grados Fahrenheit es de: {(9/5)*temp_c+32}")

#10)
num=float(input("Ingrese el primer numero: "))
num2=float(input("Ingrese el segundo numero: "))
num3=float(input("Ingrese el tercer numero: "))
print(f"El promedio es: {(num+num2+num3)/3}")