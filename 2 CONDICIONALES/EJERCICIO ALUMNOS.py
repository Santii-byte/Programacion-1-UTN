fecha=input('Ingrese el dia y fecha actual en el formato sin tilde "dia, DD/MM" ')
long=len(fecha)
dia_mes=fecha[long-5:long-3]
mes=(fecha[long-2:long])
dia=fecha[0:long-7]
dia=dia.lower()

if dia_mes[0]=='0':
    dia_mes=int(dia_mes[1])
else:
    dia_mes=int(dia_mes)
if mes[0]=='0':
    mes=int(mes[1])
else:
    mes=int(mes)

if dia_mes<1 or dia_mes>31:
    print(f"El dia del mes es invalido ({dia_mes})")
elif mes<1 or mes>12:
    print(f"El mes es invalido ({mes})")

elif dia!='lunes' and dia!='martes' and dia!='miercoles' and dia!='jueves' and dia!='viernes' and dia!='sabado' and dia!='domingo':
    print(f"El dia de la semana es invalido ({dia})")

else:
    if dia!='viernes' and dia!='jueves':
        examen=int(input("Este dia hubo examen? 1=si, 2=no "))
        if examen==1:
            aprobados=int(input("Cuantos alumnos aprobaron el examen? "))
            if aprobados<0:
                print(f"El numero de aprobados es invalido ({aprobados})")
            desaprobados=int(input("Cuantos alumnos desaprobaron el examen? "))
            if desaprobados<0:
                print(f"El numero de desaprobados es invalido ({desaprobados})")
            if aprobados>=0 and desaprobados>=0:
                total=aprobados+desaprobados
                porcentaje=(aprobados*100)/total
                print(f"El porcentaje de aprobados es {porcentaje}%")
                if porcentaje<50:
                    print("La mayoria de los alumnos desaprobo el examen")
                elif porcentaje==50:
                    print("La misma cantidad de alumnos aprobo y desaprobo el examen")
                else:
                    print("La mayoria de los alumnos aprobo el examen")
        elif examen==2:
            print("No hubo examen")
        else:
            print(f"Opcion invalida ({examen})")
    else:
        asistencia=int(input("No se pueden tomar examenes los jueves ni los viernes. Ingresa el numero de porcentaje de asistencia"))
        if asistencia<0 or asistencia>100:
            print(f"El porcentaje de asistencia es invalido ({asistencia})")
        else:
            if asistencia<50:
                print("La mayoria de los alumnos no asistio a clases")
            else:
                print("La mayoria de los alumnos asistio a clases")

    if dia=='viernes' and dia_mes==1 and (mes==1 or mes==7):
        alumnos=int(input("Comienzo de nuevo ciclo, ingrese la cantidad de alumnos "))
        arancel=int(input("Ingrese el arancel mensual por alumno "))
        if alumnos<0:
            print(f"La cantidad de alumnos es invalida ({alumnos})")
        elif arancel<0:
            print(f"El arancel es invalido ({arancel})")
        else:
            ingresos=alumnos*arancel
            print(f"Los ingresos mensuales son de ${ingresos}")

                       
        
    