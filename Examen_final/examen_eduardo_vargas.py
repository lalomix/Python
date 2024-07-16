#================Librerias================
import random  
import os
import csv
#=========================================
#================Funciones================
#funcion_menu_1
def sueldos_aleatorios():
    for workers in trabajadores:
        workers[1] = random.randint(300000,2500000)
        workers[2] = int(workers[1] * 0.07)
        workers[3] = int(workers[1] * 0.12)
        workers[4] = workers[1] - (workers[2] + workers[3])

#funcion_menu_2
def clasificar_sueldos():
    plana_mayor = 0
    plana_media = 0
    plana_baja = 0
    for workers in trabajadores:
        if workers[1] > 2000000:
            plana_mayor +=1
            workers[5] = "plana_mayor"
        elif workers[1] <= 2000000 and workers[1] >= 800000:
            plana_media +=1
            workers[5] = "plana_media"
        else:
            plana_baja +=1
            workers[5] = "plana_baja"
    print("\n")
    print(f"Sueldos menores a $800.000 TOTAL: {plana_baja}")
    print("Nombre Empleado\t\tSueldo")
    for workers in trabajadores:
        if workers[5] == "plana_baja":            
            print(f"{workers[0]}\t\t{workers[1]}")            
    print("\n")
    print(f"Sueldos entre $800.000 y $2.000.000 TOTAL: {plana_media}")
    print("Nombre Empleado\t\tSueldo")
    for workers in trabajadores:
        if workers[5] == "plana_media":            
            print(f"{workers[0]}\t\t{workers[1]}")
    print("\n")
    print(f"Sueldos superiores a $2.000.000 TOTAL: {plana_mayor}")
    print("Nombre Empleado\t\tSueldo")
    for workers in trabajadores:
        if workers[5] == "plana_mayor":            
            print(f"{workers[0]}\t\t{workers[1]}") 
 
#funcion_menu_3
def estadisticas_sueldos():
    promedio_sueldos = 0
    suma_sueldos = 0
    sueldo_alto = 0
    sueldo_bajo = 0
    salarios=[]        
    for workers in trabajadores:
        suma_sueldos=suma_sueldos + workers[1]
        salarios.append(workers[1])
    promedio_sueldos = int(suma_sueldos/10)    
    sueldo_alto = max(salarios)
    sueldo_bajo = min(salarios)
    print(f"El sueldo mas alto de la empresa es: {sueldo_alto}.\nEl mas bajo es {sueldo_bajo}.\nEl promedio de sueldos es {promedio_sueldos}")

#funcion_menu_4
def reporte_sueldos():
    with open("reporte_sueldos.csv", "w", newline="", encoding ="utf-8" ) as file_csv:
        csv_writer = csv.writer(file_csv)
        csv_writer.writerows(trabajadores)
 
#=========================================
#================Variables================
trabajadores =  (
                ["Juan Pérez","","","","",""],
                ["Carlos López","","","","",""],
                ["Ana Martínez","","","","",""],
                ["Pedro Rodríguez","","","","",""],
                ["Laura Hernández","","","","",""],
                ["Miguel Sánchez","","","","",""],
                ["Isabel Gómez","","","","",""],
                ["Francisco Díaz","","","","",""],
                ["Carlos López","","","","",""],
                ["Elena Fernández","","","","",""]
)
           
#=========================================
#==================Menú===================
while True:
    try:
        print("\n")
        print("Ingrese la opcion deseada. ")
        print("1. Asignar sueldos aleatorios. ")
        print("2. Clasificar sueldos. ")
        print("3. Ver estadísticas. ")
        print("4. Reporte de sueldos")
        print("5. Salir del programa")
        opcion=int(input(""))
        match opcion:
            case 1:
                os.system("cls")
                print("Asignando sueldos aleatorios...")
                sueldos_aleatorios()
            case 2:
                os.system("cls")
                clasificar_sueldos()
            case 3:
                os.system("cls")
                print("Mostrando Estadisticas...")
                estadisticas_sueldos()
            case 4:
                os.system("cls")
                print("\n")
                print("Mostrando Reportes...")
                reporte_sueldos()
            case 5:
                os.system("cls")
                print("Finalizando programa…")
                print("Desarrollado por Eduardo Vargas")
                print("RUT 16.001.842-9")
                break
            case _:
                print("Usted ha ingresado una opcion que no esta en el menú ")
    
    except ValueError:
        print("Ha ingresado un valor erroneo, favor reintente")


#=========================================

