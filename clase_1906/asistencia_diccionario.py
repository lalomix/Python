import os
from datetime import datetime
now = datetime.now()
alumnos=[]
fecha_asistencia=[]

#Funciones

def guardar_asistencia(alumno):
    alumnos.append(alumno)
    fecha_asistencia.append(now.strftime('%d-%m-%Y'))

def buscar_asistencia(alumno):
    if alumno in alumnos:
        i = alumnos.index(alumno)
        print(alumnos[i], fecha_asistencia[i])
    else:
        print(f"Lo siento, no encontramos registros de {alumno} en nuestro sistema de asistencia")
#Fin Funciones
validador = True
validador2 = True
while validador:
    print("\n")
    print("1. Guardar Asistencia ")
    print("2. Buscar Asistencia ")
    print("3. Salir ")
    print("4. revisar registros en array ")
    print("\n")
    opcion=(int(input("Ingrese la opcion deseada ")))
    match opcion:
        case 1:
            os.system("cls")
            while validador2:
                alumno=input("Ingrese nombre y apellido de alumno que desea registar,\n escriba terminar para finalizar: ").lower()
                if alumno == "terminar":
                    validador2 = False
                else: 
                    guardar_asistencia(alumno)
        case 2:
            os.system("cls")
            alumno=input("Ingrese el nombre y el apellido del alumno que desea buscar el registro de asistencia : ")
            buscar_asistencia(alumno)
        case 3:
            os.system("cls")
            print("Adios. ")
            validador = False
        case 4:
            os.system("cls")
            print(alumnos)
            print(fecha_asistencia)
        case _:
            os.system("cls")
            mensaje=("ERROR, INTENTE NUEVAMENTE")
        

