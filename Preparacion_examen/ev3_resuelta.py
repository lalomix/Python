
#########################################################
#  RESOLUCIÓN EVALUACIÓN 3 - FUNDAMENTOS DE PROGRAMACIÓN
#         DOUC - PLAZA VESPUCIO - VESPERTINO
#########################################################

#########################################################
#               IMPORTACION DE LIBRERÍAS
#########################################################

import csv
from datetime import datetime
#########################################################
#               DEFINICIÓN DE FUNCIONES
#########################################################


def menu():
    print("""
        Ingrese una de las siguientes opciones:
        
        1) Reservar habitación
        2) Buscar habitación
        3) Ver estado del hotel
        4) Calcular venta diaria
        5) Exportar archivo
        6) Imprimir diccionario
        7) Salir
        
        """)


def reservar_habitacion(hotel=[]):

    codigo = input("Habitación a reservar: ")
    nombre = input("Nombre del huesped: ")
    apellido = input("Apellido del huesped: ")
    rut = input("RUT del huesped: ")
    checkin = input("Fecha de ingreso: ")
    checkout = input("Fecha de salida: ")

    for habitacion in hotel:
        if habitacion[0] == codigo:
            habitacion[1] = "reservada"
            habitacion[3] = nombre
            habitacion[4] = apellido
            habitacion[5] = rut
            habitacion[6] = checkin
            habitacion[7] = checkout
            print("Habitación reservada")
            print(habitacion)
            break


def buscar_habitacion(hotel=[]):
    codigo = input("Ingrese el código de la habitación: ")
    for habitacion in hotel:
        if habitacion[0] == codigo:
            return habitacion


def ver_estado(hotel=[]):
    for habitacion in hotel:
        print(habitacion)


def venta_diaria(hotel=[]):
    total = 0
    for habitacion in hotel:
        total += habitacion[2] if habitacion[1] == "reservada" else 0
    return total


def guardar(hotel):
    with open('hotel.csv', 'w', newline='', encoding='utf-8') as csv_file:
        fieldnames = ['numero', 'estado', 'valor', 'nombre','apellido', 'rut', 'entrada', 'salida']
        hotel.insert(0,fieldnames)
        csv_writer = csv.writer(csv_file)
        csv_writer.writerows(hotel)

#########################################################
#               DESARROLLO DEL ALGORITMO
#########################################################

hotel = []
pisos = 5
habitaciones_por_piso = 8

# Se genera la lista de listas para la información necesaria por cada piso y habitación
for piso in range(1, pisos + 1):
    for habitacion in range(1, habitaciones_por_piso + 1):
        codigo = str(10 * piso + habitacion)
        if piso == 5:
            hotel.append([codigo, "disponible", 100000, "", "", "", "", ""])
        elif piso == 4:
            hotel.append([codigo, "disponible", 60000, "", "", "", "", ""])
        else:
            hotel.append([codigo, "disponible", 30000, "", "", "", "", ""])


while True:
    menu()
    opcion = input("Eliga opción (1-6): ")
    if opcion == "7":
        print("Saliendo del programa ...")
        break
    elif opcion == "1":
        reservar_habitacion(hotel)
    elif opcion == "2":
        print(buscar_habitacion(hotel))
    elif opcion == "3":
        ver_estado(hotel)
    elif opcion == "4":
        print("La venta del día tiene un total de: ", venta_diaria(hotel))
    elif opcion == "5":
        guardar(hotel)
    elif opcion == "6":
        print(hotel)    
    else:
        print("Seleccionar una opción correcta.")
