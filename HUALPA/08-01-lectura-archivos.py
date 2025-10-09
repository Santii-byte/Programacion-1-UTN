# -*- coding: utf-8 -*-

# Nombre del archivo que queremos leer (ruta relativa)
#RUTA_ARCHIVO = "C:\\Users\\hualp\\OneDrive\\Escritorio\\listaAlumnos.txt"
#RUTA_ARCHIVO = r"C:\Users\hualp\OneDrive\Escritorio\listaAlumnos.txt"



#RUTA_ARCHIVO = "C:\Users\hualp\OneDrive\Escritorio\listaAlumnos.txt"






RUTA_ARCHIVO = "./listaAlumnosC4.txt"



try:
    # Abrimos el archivo en modo lectura
    archivo = open(RUTA_ARCHIVO, "r", encoding="utf-8")
    #archivo = open(RUTA_ARCHIVO, "r")
    contenido=archivo.read()
    print("Contenido del archivo:\n")

    lista=contenido.strip().split(";")
    for i in lista:
        print(i)

except FileNotFoundError:
    print(f"Error: no se encontró el archivo '{RUTA_ARCHIVO}'. Verificá la ruta o el nombre.")
except PermissionError:
    print(f"Error: no tenés permisos para leer el archivo '{RUTA_ARCHIVO}'.")
except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")
finally:
    # Cerramos el archivo si fue abierto correctamente
    try:
        archivo.close()
    except NameError:
        # Si el archivo nunca se abrió, evitamos error en close()
        pass
