alumnos=[]
asistencias=[]

while True:
    opcion=input("""MENU
    1. Ingresar alumnos
    2. Mostrar listado de asistencias
    3. Consultar asistencia por estudiante
    4. Listar estudiantes con asistencia 0
    5. Marcar asistencia
    0. Salir
    Ingrese una opcion: """)
    if opcion=="1":
        while True:
            nombre=input("Ingrese el nombre del alumno (o 'fin' para terminar): ")
            if nombre.lower()=="fin":
                break
            alumnos.append(nombre)
            asistencias.append(0)
        input("Pulse Enter para continuar...")
    elif opcion=="2":
        print("Listado de asistencias:")
        for i in range(len(alumnos)):
            print(f"{alumnos[i]}: {asistencias[i]} asistencias")
        input("Pulse Enter para continuar...")
    elif opcion=="3":
        nombre=input("Ingrese el nombre del estudiante a consultar: ")
        if nombre in alumnos:
            index=alumnos.index(nombre)
            print(f"El alumno {nombre} tiene {asistencias[index]} asistencias.")
        else:
            print("Estudiante inexistente.")
    elif opcion=="4":
        for i in range(len(alumnos)):
            if asistencias[i]==0:
                print(f"{alumnos[i]} {asistencias[i]} asistencias.")
        input("Pulse Enter para continuar...")
    elif opcion=="5":
        nombre=input("Ingrese el nombre del estudiante a marcar asistencia: ")
        if nombre in alumnos:
            asis=int(input("Ingrese cuantas asistencias sumarle: "))
            index=alumnos.index(nombre)
            asistencias[index]+=asis
    elif opcion=="0":
        print("Terminando programa...")
        break

    