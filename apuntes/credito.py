print("\n")
print("*********************************************************")
print("             Bienvenido al Banco Duoc UC                 ")
print("*********************************************************")
print("\n")

cupo_total = 1000000
deuda_total = 100000
opcion_usuario = 0
validador = True
abono_deuda = 0
total_compra = 0


while validador == True:
    try:
        print("Ingrese la opción que desea \n")
        while opcion_usuario != 3:
            opcion_usuario = int(input("1. Pago de Tarjeta de Credito\n2. Simulacion de Compra\n3. Salir \n"))
            if opcion_usuario == 3:
                validador = False
            elif opcion_usuario > 3:
                print(" Ha ingresado una opción que no esta en el menú, intente nuevamente\n")
            elif opcion_usuario == 1:
                print(" Ha ingresado a la opción - Pago de Tarjeta de credito \n")
                abono_deuda = int(input(f"Su deuda actual es de: {deuda_total}. \nSu cupo actual disponible es: {cupo_total - deuda_total}. \nIngrese el monto que desea abonar a su tarjeta\n"))
                if abono_deuda > 0 and abono_deuda <= deuda_total:
                    deuda_total -= abono_deuda 
                    print(f"Usted ha abonado {abono_deuda} a su cuenta, su nuevo total es {cupo_total - deuda_total}")
                else:
                    print("Mono invalido o superior a la deuda actual, favor reintente!")    
            else:
                compra_compulsiva = True
                while compra_compulsiva == True:
                    compra_usuario = int(input("Ingrese el monto de la compra que esta realizando.\n"))
                    if compra_usuario >0:
                        total_compra += compra_usuario
                        print(f"ha realizado una compra de {compra_usuario}, su nuevo cupo disponible es {cupo_total - compra_usuario}")
                        seguir_comprando= int(input("Desea seguir comprando? 1. SI 2. NO \n"))                             
                        if seguir_comprando == 2:
                            print("Saliendo del modulos compras")
                            break

                    else:
                        print("Monto invalido!")

    except ValueError:
        print(" \n Ha ingresado una opcion o dato no valido!, favor reintente. \n")


print ("Gracias por preferir Banco Duoc UC, Adios!")


# Descripción de la Actividad:

# El programa debe tener un menú de opciones de donde se pueda realizar el pago del cupo de la tarjeta de crédito, como también simular nuevas compras, y estas una vez sumadas se resten al cupo disponible. 
# Las opciones disponibles deben estar construidas de la siguiente forma:
# 1.	Pago de Tarjeta de Crédito:
# a.	El usuario comienza con una deuda de $100.000
# b.	El usuario puede ingresar un monto para realizar un pago en la tarjeta de crédito.
# c.	Se debe verificar que el monto ingresado sea mayor o igual a cero.
# d.	Se debe verificar que el monto a pagar no exceda el saldo actual de la tarjeta.
# e.	Al pagar el sistema debe descontar de la deuda total
# f.	Si las verificaciones son exitosas, se realiza el pago y se actualiza el saldo de la tarjeta.
# 2.	Simulación de Compras:
# a.	El usuario puede simular realizar un número ilimitado de compras.
# b.	Para cada compra, se solicita al usuario ingresar el monto de la compra. El programa suma los montos de cada compra. 
# c.	Se verifica que el monto de la compra sea mayor o igual a cero.
# d.	Se realiza la compra y se actualiza el saldo de la tarjeta para cada iteración del bucle for.
# 3.	Salir:
# a.	Al seleccionar esta opción, el programa debe cerrarse o finalizar.

# A considerar:
# 1.	Manejo de Errores:
# a.	Se utilizan bloques try y except para manejar posibles errores al ingresar datos, validar valores no numéricos y errores inesperados. 
# b.	Se debe programar mensajes de error específicos para guiar al usuario sobre posibles problemas.


# Instrucciones para el envío de la actividad

# El estudiante deberá comprimir los programas y enviar al docente a través de Mensajes de AVA, utilizando el siguiente formato para el nombre del archivo:
# NombreApellido.RAR
