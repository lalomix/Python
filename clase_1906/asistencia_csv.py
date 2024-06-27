import os
import csv
from datetime import datetime
now = datetime.now()
alumnos=[]
asistencia_recuperados =[]
fecha_asistencia=[]
fecha_seteada=now.strftime('%d-%m-%Y')
#Funciones

def guardar_asistencia(alumnos):    
    with open(f"Asistencia_{fecha_seteada}.csv", "w") as file:
        for i in range(len(alumnos)):
            file.write(f"{alumnos[i]},{fecha_asistencia[i]} \n")  

def buscar_asistencia(alumno):
    with open(f"Asistencia_{fecha_seteada}.csv", "r", newline="") as csv_file:
        lector_csv = csv.reader(csv_file, delimiter=",")
        for fila in lector_csv:
    	    asistencia_recuperados.append(fila)
        print(asistencia_recuperados)
        if alumno in asistencia_recuperados:
            i = asistencia_recuperados.index(alumno)
            print(asistencia_recuperados[i])
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
                    guardar_asistencia(alumnos)
                else:
                    alumnos.append(alumno)
                    fecha_asistencia.append(fecha_seteada)
        case 2:
            os.system("cls")
            alumno=input("Ingrese el nombre y el apellido del alumno que desea buscar el registro de asistencia : ").lower()
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
        

