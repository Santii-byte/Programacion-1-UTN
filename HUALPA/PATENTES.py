abc=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
num=["0","1","2","3","4","5","6","7","8","9"]
contador=0

elec=input("Desea buscar la patente en el sistema o ingresar una posicion de patente? (1/2): ")

if elec=="2":
    pos=int(input("Ingrese la posicion de la patente que desea conocer (1-175760000): "))
    if pos<1 or pos>175760000:
        print("La posicion no es valida")
    else:
        for i in abc:
            for j in abc:
                for k in abc:
                    for l in num:
                        for m in num:
                            for n in num:
                                contador+=1
                                if contador==pos:
                                    print(f"La patente en la posicion {pos} es: {i}{j}{k}{l}{m}{n}")
                                    break

elif elec=="1":
    patente=input("Ingrese la patente del vehiculo: ").upper()

    if len(patente)==6:
        if patente[0] in abc and patente[1] in abc and patente[2] in abc and patente[3] in num and patente[4] in num and patente[5] in num:
            print("La patente es valida")
        else:
            print("La patente no es valida")
    else:
        print("La patente no es valida")

    for i in abc:
            for j in abc:
                for k in abc:
                    for l in num:
                        for m in num:
                            for n in num:
                                contador+=1
                                if i==patente[0] and j==patente[1] and k==patente[2] and l==patente[3] and m==patente[4] and n==patente[5]:
                                    print(f"La patente se encontro en la posicion:{contador}")
                                    break

