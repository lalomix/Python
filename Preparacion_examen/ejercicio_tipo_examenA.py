#============Librerias===============
import csv
from datetime import datetime
import os
import random
import time
#====================================

#============Funciones===============

#funcion menu 1
def sueldos_aleatorios():
    for sueldos in trabajadores:
        sueldos["sueldo"] = random.randint(500000, 5000000)

#funcion menu 2
def clasificacion_sueldos():
    for clasificacion in trabajadores:
        if clasificacion["sueldo"] > 2000000:
            clasificacion["clasificacion"] = "plana_mayor"
        elif clasificacion["sueldo"] >=800000 and clasificacion["sueldo"] <= 2000000:
            clasificacion["clasificacion"] = "plana_media"
        else:
            clasificacion["clasificacion"] = "plana_baja"
    
#funcion menu 3
def exportar_sueldos():
    with open('sueldos.csv', 'w', newline='', encoding='utf-8') as csv_file:
        fieldnames = ['nombre', 'cargo', 'sueldo', 'clasificacion']
        escritor_csv = csv.DictWriter(csv_file, fieldnames)
        escritor_csv.writerows(trabajadores)
        

#====================================

#============Variables===============

trabajadores = [
    {"nombre": "Juan Pérez", "cargo": "Consultor TI"},
    {"nombre": "María García", "cargo": "Analista"},
    {"nombre": "Carlos López", "cargo": "Programador"},
    {"nombre": "Ana Martínez", "cargo": "Jefe de Proyecto"},
    {"nombre": "Pedro Rodríguez", "cargo": "Consultor TI"},
    {"nombre": "Laura Hernández", "cargo": "Analista"},
    {"nombre": "Miguel Sánchez", "cargo": "Programador"},
    {"nombre": "Isabel Gómez", "cargo": "Jefe de Proyecto"},
    {"nombre": "Francisco Díaz", "cargo": "Consultor TI"},
    {"nombre": "Elena Fernández", "cargo": "Analista"}
]
#====================================

#==============Menú==================
while True:
    try:
        print("\n")
        print("Ingrese la opcion deseada ")
        print("1. Asignar sueldos aleatorios ")
        print("2. Clasificar Sueldos ")
        print("3. Exportar sueldos ")
        print("4. Salir ")
        print("\n")
        opcion=int(input(""))
        match opcion:
            case 1:
                os.system("cls")
                print("Asignando sueldos aleatoreamente...")
                time.sleep(3)
                sueldos_aleatorios()
            case 2:
                os.system("cls")
                print("Clasificando sueldos...")
                time.sleep(3)
                clasificacion_sueldos()
            case 3:
                os.system("cls")
                print("Exportando sueldos...")
                time.sleep(3)
                exportar_sueldos()
            case 4:
                os.system("cls")
                print("Saliendo...")
                time.sleep(3)
                break                
            case _:
                print("Opción del menú invalida ")
    
    
    except ValueError:
        print("Lo sentimos, ha ingresado un valor no valido, favor reintente. ")
            
    
#====================================


