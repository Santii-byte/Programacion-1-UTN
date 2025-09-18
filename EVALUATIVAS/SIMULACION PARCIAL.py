titulos=[]
ejemplares=[]
opcion=""
while opcion != "10":
    opcion=input("""Elija una opcion: 
    1. Ingresar titulos 
    2. Ingresar ejemplares 
    3. Mostrar catalogo con stock 
    4. Buscar libro 
    5. Listar agotados 
    6. Agregar titulo 
    7. Ver titulos agotados
    8. Actualizar ejemplares 
    9. Ver catologo completo 
    10. Salir
    Opcion: """
        )
    if opcion=="1":
        titulo=""
        while True:
            titulo=input("Ingrese el titulo del libro o 0 para parar: ")
            if titulo=="0":
                break
            else:
                titulos.append(titulo)
                ejemplares.append(0)
        print(f"Titulos ingresados: {titulos}")
        input("Presione Enter para continuar...")
    elif opcion=="2":
        ejemplar=0
        for i in range(len(titulos)):
            ejemplar=int(input(f"Ingrese la cantidad de ejemplares para {titulos[i]}"))
            ejemplares[i]=ejemplar
            input("Presione Enter para continuar...")
    elif opcion=="3":
        for i in range(len(titulos)):
            if ejemplares[i]>0:
                print(f"{titulos[i]} - {ejemplares[i]} ejemplares")
        input("Presione Enter para continuar...")
    elif opcion=="4":
        buscar=input("Ingrese el titulo del libro a buscar: ")
        if buscar in titulos:
            indice=titulos.index(buscar)
            print(f"{titulos[indice]} - {ejemplares[indice]} ejemplares")
        else:
            print("El libro no se encuentra en el catalogo")
        input("Presione Enter para continuar...")
    elif opcion=="5":
        for i in range(len(titulos)):
            if ejemplares[i]==0:
                print(f"{titulos[i]} - Agotado")
        input("Presione Enter para continuar...")
    elif opcion=="6":
        nuevo_titulo=input("Ingrese el nuevo titulo: ")
        titulos.append(nuevo_titulo)
        nuevo_ejemplar=int(input("Ingrese la cantidad de ejemplares: "))
        ejemplares.append(nuevo_ejemplar)
        print(f"Nuevo titulo {nuevo_titulo} con {nuevo_ejemplar} ejemplares agregado")
        input("Presione Enter para continuar...")
    elif opcion=="7":
        for i in range(len(titulos)):
            if ejemplares[i]==0:
                print(f"{titulos[i]} - Agotado")
        input("Presione Enter para continuar...")
    elif opcion=="8":
        actualizar_titulo=input("Ingrese el titulo del libro a actualizar: ")
        if actualizar_titulo in titulos:
            indice=titulos.index(actualizar_titulo)
            nuevo_ejemplar=int(input(f"Ingrese la nueva cantidad de ejemplares para {actualizar_titulo}: "))
            ejemplares[indice]=nuevo_ejemplar
            print(f"Cantidad de ejemplares para {actualizar_titulo} actualizada a {nuevo_ejemplar}")
        else:
            print("El libro no se encuentra en el catalogo")
        input("Presione Enter para continuar...")
    elif opcion=="9":
        for i in range(len(titulos)):
            print(f"{titulos[i]} - {ejemplares[i]} ejemplares")
        input("Presione Enter para continuar...")
    elif opcion=="10":
        print("Saliendo del programa...")
    