#===================Librerias========================
import os
import time

#====================================================
#===================Funciones========================
#funcion_menu_1

def registrar_trabajador(id, nombre_trabajador, cargo_trabajador,sueldobruto_trabajador):
    global porcentaje_salud 
    global porcentaje_afp
    salud = int(sueldobruto_trabajador*porcentaje_salud)
    afp = int(sueldobruto_trabajador*porcentaje_afp)
    sueldo_liquido = int(sueldobruto_trabajador -(salud+afp))
    trabajadores[id] = {"nombre": nombre_trabajador, "cargo": cargo_trabajador, "sueldo_bruto": sueldobruto_trabajador, "descuento_salud": salud, "descuento_afp": afp, "total_pago": sueldo_liquido }
    
#funcion_menu_2
def listar_trabajadores():
    print("Trabajador\t\t\tCargo\t\t\tSueldo Bruto\tSalud\tAFP\tLiquido a pagar")
    for x in trabajadores:
        print(f"{trabajadores[x]["nombre"]}\t\t\t{trabajadores[x]["cargo"]}\t\t\t{trabajadores[x]["sueldo_bruto"]}\t{trabajadores[x]["descuento_salud"]}\t{trabajadores[x]["descuento_afp"]}\t{trabajadores[x]["total_pago"]}" )
    time.sleep(10) # informacion se muestra en pantalla por 10 segundos y vuelve al menu
    
    
#funcion_menu_3

def exportar_remuneraciones():
    with open('listado_trabajadores.txt', 'w') as file:
        file.write("Trabajador\t\t\tCargo\t\t\tSueldo Bruto\tSalud\tAFP\tLiquido a pagar\n")
        for x in trabajadores:
            file.write(f"{trabajadores[x]["nombre"]}\t\t\t{trabajadores[x]["cargo"]}\t\t\t{trabajadores[x]["sueldo_bruto"]}\t{trabajadores[x]["descuento_salud"]}\t{trabajadores[x]["descuento_afp"]}\t{trabajadores[x]["total_pago"]}\n" )

#====================================================    
#===================Variables========================
validador=True
id=0
porcentaje_salud = 0.07
porcentaje_afp = 0.12
trabajadores = {}

#====================================================
#===================Menu=============================
while validador:
    try:
        print("\n")
        print("Ingrese la opcion deseada ")
        print("\n")
        print("1. Registrar Trabajador ")
        print("2. Listar todos los trabajadores ")
        print("3. imprimir planilla de sueldos ")
        print("4. Salir ")
        print("\n")
        opcion=(int(input()))
        match opcion:
            case 1:
                validador2=True
                os.system("cls")
                print("Registro de trabajadores ")
                print("\n")
                id+=1
                nombre_trabajador=(input("Ingrese el nombre y apellido del nuevo trabajador:  ")).title()
                while validador2:
                    print("Seleccione el cargo correspondiente segun el siguiente listado: \n 1. CEO\n 2. Desarrollador\n 3. Analista de Datos\n  ")
                    opc_cargo=(int(input(" ")))
                    if opc_cargo == 1:
                        cargo_trabajador = "CEO              "
                        validador2 = False
                    elif opc_cargo == 2:
                        cargo_trabajador = "Desarrollador    "
                        validador2 = False
                    elif opc_cargo == 3:        
                        cargo_trabajador = "Analista de datos"
                        validador2 = False
                    else:
                        os.system("cls")
                        print("Ha ingresado una opción de cargo no válida, favor reintente")
                        time.sleep(2) # informacion se muestra en pantalla por 2 segundos y vuelve al menu
                sueldobruto_trabajador=(int(input("Ingrese el sueldo bruto que recibirá el trabajador mensualmente: ")))
                                            
                
                registrar_trabajador(id, nombre_trabajador, cargo_trabajador,sueldobruto_trabajador)
            case 2:
                os.system("cls")
                print("A continuacion el listado de trabajadores de la empresa: ")
                print("\n")
                listar_trabajadores()

            case 3:
                os.system("cls")
                exportar_remuneraciones()
                print("Exportando Remunerciones ")
                time.sleep(5) # informacion se muestra en pantalla por 5 segundos y vuelve al menu
            case 4:
                os.system("cls")
                print("Gracias por preferir sistema de sueldos DuocUC, Adios. ")
                validador = False
                time.sleep(2)  # informacion se muestra en pantalla por 2 segundos y vuelve al menu
            case _:
                os.system("cls")
                print("Opcion del menú invalido, Intente Nuevamente")   
            
    except ValueError:
        os.system("cls")
        print("Ha ingresado un dato no valido, favor reintente")
        time.sleep(5) # informacion se muestra en pantalla por 5 segundos y vuelve al menu
#====================================================


    