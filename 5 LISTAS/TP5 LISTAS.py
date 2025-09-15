#1)
lista=list(range(4,101,4))
print (lista)

#2)
lista=[2,4,1,3]
print(lista[-2])

#3)
lista=[]
lista.append("Hola")
lista.append("Mundo")
lista.append("Python")
print (lista)

#4)
animales = ["perro", "gato", "conejo", "pez"]
animales[1]="loro"
animales[-1]="oso"
print(animales)

#5)
# Este codigo ncuentra el valor maximo de la lista - max(numeros) = 22
# y despues lo elimina de la lista con remove()
numeros = [8, 15, 3, 22, 7]
numeros.remove(max(numeros))
print(numeros)

#6)
lista=list(range(10,31,5))
print(lista[0], lista[1])

#7)
autos = ["sedan", "polo", "suran", "gol"]
autos[1:3] = ["fiesta", "corsa"]

#8)
dobles=[]
[dobles.append(x) for x in [5*2, 10*2, 15*2]]
print(dobles)

#9)
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
compras[2].append("jugo")
compras[1][1]="tallarines"
compras[0].remove("pan")
print(compras)

#10)
lista_anidada=[15,True, [25.5, 57.9, 30.6], False]
print(lista_anidada)
