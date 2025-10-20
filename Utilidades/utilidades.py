#Instrucciones basicas para listas


frutas = ["manzana", "banana", "cereza"]

# Acceder a un rango (slicing)
print(frutas[0:2])  # ["manzana", "banana"]

# Reemplazar varios elementos usando slicing
frutas[0:2] = ["pera", "uva"]
print(frutas) # ["pera", "uva", "cereza"]



#AGREGAR ELEMENTOS

# Al final de la lista
frutas.append("naranja")  # ["pera", "uva", "cereza", "naranja"]

# En una Posición específica
frutas.insert(1, "mango") # ["pera", "mango", "uva", "cereza", "naranja"]

# Agregar otra lista
frutas.extend(["kiwi", "limón"])  # ["pera", "mango", "uva", "cereza", "naranja", ["kiwi", "limón"]]



#ELIMINAR ELEMENTOS

# Por valor (elimina la primera coincidencia)
frutas.remove("uva")  # ["pera", "mango", "cereza", "naranja", "kiwi", "limón"]

# Por índice
del frutas[2]         # elimina "cereza"
print(frutas)         # ["pera", "mango", "naranja", "kiwi", "limón"]

# Eliminar y obtener el elemento
eliminado = frutas.pop(1)  # elimina "mango" y lo guarda en 'eliminado'

# Vaciar lista
frutas.clear()  # lista queda []



#BUSCAR ELEMENTOS

print("kiwi" in frutas)  # True o False
print(frutas.index("kiwi"))  # devuelve índice



#OTROS UTILES
# Tamaño de la lista
len(frutas)

# Ordenar
frutas.sort()         # alfabéticamente
frutas.sort(reverse=True)  # descendente

# Invertir orden
frutas.reverse()
