#1 
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':1450}
precios_frutas.update({"Naranja": 1200, "Manzana": 1500, "Pera": 2300})
print(precios_frutas)

#2
precios_frutas.update({"Banana": 1330, "Manzana": 1700, "Melón": 2800})
print(precios_frutas)

#3
frutas = list(precios_frutas.keys())
print(frutas)

#4
telef={}
for i in range(5):
    nombre=input("Ingrese un nombre: ")
    numero=int(input(f"Ingrese el numero para {nombre}: "))
    telef.update({f"{nombre}":{numero}})
nombre=input("Ingrese el nombre a buscar: ")
print(f"El numero perteneciente a {nombre} es: ",telef.get(f"{nombre}", "No encontrado"))  

#5
frase=input("Ingrese una frase: ")
frase_l=frase.split()
conteo = {}
for palabra in frase_l:
    if palabra in conteo:
        conteo[palabra] += 1
    else:
        conteo[palabra] = 1
frase_s=set(frase_l)
print(f"Set de la frase: {frase_s}")
print(f"Diccionario: {conteo}")

#6
alumnos={}

for i in range(3):
    nombre=input(f"Ingrese el alumno {i+1}: ")
    notas=[]
    for j in range(3):
        nota=int(input(f"Ingrese la nota {j+1}: "))
        notas.append(nota)
    alumnos[nombre]=tuple(notas)

for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"El promedio de {nombre} es: {promedio:.2f}")

#7
parcial1 = {1, 2, 3, 4, 5}
parcial2 = {4, 5, 6, 7}

ambos = parcial1 & parcial2
solo_uno = parcial1 ^ parcial2
al_menos_uno = parcial1 | parcial2

print("Aprobaron ambos:", ambos)
print("Aprobaron solo uno:", solo_uno)
print("Aprobaron al menos un parcial:", al_menos_uno)

#8
inventario={
    "Manzanas": 5,
    "Peras": 3,
    "Bananas": 7
}
while True:
    opcion=input("Ingrese un producto, 0 para parar ")
    if opcion=="0":break
    if opcion in inventario:
        ingreso=int(input("Producto encontrado, ingresar unidades a sumar: "))
        inventario.update({f"{opcion}": inventario[opcion]+ingreso})
        print(f"Ahora contamos con {inventario[opcion]} {opcion}")
    else:
        ingreso=int(input("Producto no encontrado, sera ingresado al inventario... Ingrese cantidad de unidades: "))
        inventario.update({f"{opcion}": ingreso})
        print(f"Se ingresaron {ingreso} {opcion}(s) correctamente.")

#9
agenda = {
    ("lunes", "10:00"): "Reunión",
    ("lunes", "12:00"): "Almuerzo",
    ("martes", "12:00"): "Gimnasio"
}
consulta = input("Ingrese el día y horario a consultar (ej: lunes 10:00): ")
lista = consulta.split()
clave = (lista[0], lista[1])
if clave in agenda:
    print(f"El evento del día {lista[0]} a las {lista[1]}hs es: {agenda[clave]}")
else:
    print("No hay evento registrado para ese día y hora.")

#10
paises = {
    "Argentina": "Buenos Aires",
    "Chile": "Santiago",
    "Perú": "Lima",
    "Uruguay": "Montevideo"
}
capitales = {} 
for pais, capital in paises.items():
    capitales[capital] = pais  # Invertimos clave y valor
print("Original: ",paises)
print("Invertido: ",capitales)
