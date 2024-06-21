# crear un programa que permita contabilizar la asistencia a clases.
# se debe guardar la asistencia en un archivo csv con fecha incluida automaticamente
# tiene que existir un menu principal que pregunte si se quiere guardar asistencia o buscar
# si se elige guardar, el programa pregunta constantemente el nombre del estudiante y si esta o no presente.
# esto se debe realizar hata que el usuario decida no seguir guardando asistencia.

# si se elige buscar, el programa debe pedir el nombre del estudiante y la fecha.
# debe devolver si el alumno estuvo o no presente ese decida

# se deben generar 2 funciones, una para guardar y otra para leer

import os
validador = True
mensaje="Bienvenidos "
while validador:
    print("=================================")
    print("             ASISTENCIA          ")
    print("=================================")
    print("\n")
    print(mensaje)
    print("\n")
    print("1. Guardar Asistencia ")
    print("2. Buscar Asistencia ")
    print("3. Salir ")

    opcion=(int(input("Ingrese la opcion deseada ")))
    match opcion:
        case 1:
            mensaje=("opcion 1")
            nombre_alumno=inpunt("Ingrese el nombre del alumno que desea registar")
        case 2:
            mensaje=("opcion 2")
        case 3:
            os.system("cls")
            print("Adios. ")
            validador = False
        case _:
            os.system("cls")
            mensaje=("OPCION ERRONEA!!!!")
        

