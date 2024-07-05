"""
crear un programa que permita contabilizar la asistencia a clases.
se debe guardar la asistencia en un archivo csv con fecha incluida automaticamente
tiene que existir un menu principal que pregunte si se quiere guardar asistencia o buscar
si se elige guardar, el programa pregunta constantemente el nombre del estudiante y si esta o no presente.
esto se debe realizar hasta que el usuario decida no seguir guardando asistencia.

si se elige buscar, el programa debe pedir el nombre del estudiante y la fecha.
debe devolver si el alumno estuvo o no presente ese dia

se deben generar 2 funciones, una para guardar y otra para leer

def guardar_asistencia(nombre= "nombre como string", asistencia=false)
def buscar_asistencia(nombre="nombre como string", asistencia = "30-06-2024")
"""

################################################################################
#                           IMPORTACION DE LIBRERIAS
################################################################################

from datetime import datetime
import csv

################################################################################
#                           DEFINICION DE FUNCIONES
################################################################################

def guardar_asistencia(lista, nombre = '',asistencia = 0):
    date = datetime.now().strftime("%d-%m-%Y")
    lista.append([nombre,asistencia,date])
    return lista

def buscar_asistencia(nombre = '',fecha = ''):
    with open('asistencia.csv','r',newline='') as archivo_csv:
        reader = csv.reader(archivo_csv)
        for fila in reader:
            if(fila[0] == nombre and fila[2] == fecha):
                return 'El esutiante estuvo ' + fila[1]
        return 'No hay datos'
    
################################################################################
#                           COMIENZO DEL PROGRAMA
################################################################################

lista_asistencia = []

while True:
    option = int(input("Eliga una opción: \n 1) Guardar asistencia \n 2) Buscar asistencia \n 3) Salir \n"))
    if option == 1:
        continuar = True
        while continuar:
            nombre = input("Ingrese nombre: ")
            asistencia = input("Ingrese si estuvo presente o ausente: ")
            lista_asistencia = guardar_asistencia(lista_asistencia, nombre=nombre,asistencia=asistencia)
            respuesta = input("Desea continuar? (si/no)")
            if respuesta == 'no':
                with open('asistencia.csv','w',newline='') as archivo_csv:
                    writer = csv.writer(archivo_csv)
                    writer.writerows(lista_asistencia)
                continuar = False
    elif option ==2:
        nombre = input("Ingrese nombre: ")
        fecha = input("Ingrese una fecha en este formato (ejemplo 30-06-2024): ")
        print(buscar_asistencia(nombre=nombre,fecha=fecha))
    elif option == 3:
        break
    else:
        print('Opción no válida')
