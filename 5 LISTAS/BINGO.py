import random
numeros_=list(range(1, 51))
bingo = False
numeros = random.sample(range(1, 51), 25)  # sample asegura que no se repitan

carton = [numeros[i:i+5] for i in range(0, 25, 5)]

for fila in carton:
    print(fila)

print("\n¡Bienvenido al juego de Bingo!")

while not bingo:
    numero_sacado = random.choice(numeros_)
    numeros_.remove(numero_sacado)
    print(f"\nNúmero sacado: {numero_sacado}")

    # Marcar el número en el cartón si está
    for i in range(5):
        for j in range(5):
            if carton[i][j] == numero_sacado:
                print("¡Número encontrado en el cartón!")
                carton[i][j] = 0

    # Mostrar el cartón actualizado
    for fila in carton:
        print(fila)

    # Verificar si todos los elementos son cero (¡Bingo!)
    bingo = all(elemento == 0 for fila in carton for elemento in fila)

    if bingo:
        print("\n¡Bingo! Has ganado el juego.")


