# 1) Imprimir numeros del 0 al 100
for i in range(101):
    print(i)

# 2) Contar la cantidad de digitos de un numero
num = int(input("Ingrese un numero entero: "))
print("Cantidad de digitos:", len(str(abs(num))))

# 3) Sumar numeros entre dos valores
a = int(input("Ingrese el primer numero: "))
b = int(input("Ingrese el segundo numero: "))
suma = 0
for i in range(min(a,b)+1, max(a,b)):
    suma += i
print("Suma de los numeros entre los dos valores:", suma)

# 4) Sumar numeros ingresados hasta que se ingrese 0
total = 0
while True:
    n = int(input("Ingrese un numero (0 para salir): "))
    if n == 0:
        break
    total += n
print("Total acumulado:", total)

# 5) Juego: adivinar un numero entre 0 y 9
import random
numero = random.randint(0, 9)
intentos = 0
while True:
    intento = int(input("Adivine el numero (0-9): "))
    intentos += 1
    if intento == numero:
        break
print("¡Correcto! Numero de intentos:", intentos)

# 6) Imprimir numeros pares del 0 al 100 en orden decreciente
for i in range(100, -1, -1):
    if i % 2 == 0:
        print(i)

# 7) Sumar todos los numeros desde 0 hasta un numero indicado
n = int(input("Ingrese un numero entero positivo: "))
suma = 0
for i in range(n+1):
    suma += i
print("La suma de todos los números desde 0 hasta", n, "es:", suma)