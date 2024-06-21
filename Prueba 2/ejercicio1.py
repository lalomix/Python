# 1.-Desarrolle un programa que simule un sistema de ventas de una tienda, donde el usuario pueda seleccionar productos para comprar. 
# Cada producto tiene un número asociado y un precio. El usuario puede seleccionar los productos que desea comprar ingresando el número correspondiente. 
# Una vez que el usuario haya terminado de seleccionar sus productos, puede elegir la opción de pagar para finalizar la compra. 
# El programa calculará el total a pagar, incluyendo el impuesto al valor agregado (IVA) del 19% (25 puntos). 

# Los productos son:
# 1.	Arroz $3150
# 2.	Aceite $1990
# 3.	Queso $2150
# 4.	Leche $1190

import os

mensaje = "Seleccione el producto que desea agregar a su pedido: "
validador = True
total_cuenta = 0


print("=====================")
print("     BIENVENIDOS A   ")
print("      DUOC STORE     ")
print("=====================")
while validador:
    try:
        print("\n")
        print(mensaje)
        print("\n")
        print("1. Arroz     $3150")
        print("2. Aceite    $1990")
        print("3. Queso     $2150")
        print("4. Leche     $1190")
        print("5. Pagar y Salir ")
        print("\n")
        opcion_usuario = int(input("Ingrese el número del articulo que desea agregar a su compra "))
        match opcion_usuario:
            case 1:
                os.system("cls")
                mensaje = "Arroz agregado correctamente! "
                total_cuenta +=3150 
            case 2:
                os.system("cls")
                mensaje = "Aceite agregado correctamente! "
                total_cuenta +=1990
            case 3:
                os.system("cls")
                mensaje = "Queso agregado correctamente! "
                total_cuenta +=2150
            case 4:
                os.system("cls")
                mensaje = "Leche agregado correctamente! "
                total_cuenta +=1190
            case 5:
                os.system("cls")
                validador = False
            case _:
                os.system("cls")
                mensaje = "Producto no encontrado, favor reintente! "
        
    except ValueError:
        os.system("cls")
        mensaje = "Ha ingresado un dato no valido, favor reintente"
print("\n")         
print(f"El total a pagar por su pedido es de: ${int(total_cuenta * 1.19)}, Gracias por su compra!")
print("\n")