validador = True
contador_opcion1 = 0
contador_opcion2 = 0
contador_opcion3 = 0
contador_opcion4 = 0
contador_opcion5 = 0
contador_general = 0
contador_dinero = 0
descuento_compra = 0
descuento_aplicable = 0
mensaje = ""

while validador == True:
    print("=======================================")
    print("              Bienvenidos              ")
    print("=======================================")
    print(mensaje)
    print("\n")
    print("1. Opcion 1 - Arroz")
    print("2. Opcion 2 - Tallarines")
    print("3. Opcion 3 - Leche")
    print("4. Opcion 4 - Huevos")
    print("5. Opcion 5 - Harina")
    print("6. Pagar y Salir   ")
    print("\n")
    opcion_usuario = int(input("Ingrese la opcion que desea "))
    match opcion_usuario:
        case 1:
            mensaje = "Se ha agregado correctamente Arroz a su pedido"
            contador_dinero = contador_dinero + 2000
            contador_opcion1 = contador_opcion1 + 1 
            contador_general = contador_general + 1
        case 2:
            mensaje = "Se ha agregado correctamente Tallarines a su pedido"
            contador_dinero = contador_dinero + 4000
            contador_opcion2 = contador_opcion2 + 1
            contador_general = contador_general + 1
        case 3:
            mensaje = "Se ha agregado correctamente Leche a su pedido"
            contador_dinero = contador_dinero + 5000
            contador_opcion3 = contador_opcion3 + 1
            contador_general = contador_general + 1
        case 4:
            mensaje = "Se ha agregado correctamente Huevos a su pedido"
            contador_dinero = contador_dinero + 6000
            contador_opcion4 = contador_opcion4 + 1
            contador_general = contador_general + 1
        case 5:
            mensaje = "Se ha agregado correctamente Harina a su pedido"
            contador_dinero = contador_dinero + 1000
            contador_opcion5 = contador_opcion5 + 1
            contador_general = contador_general + 1
        case 6:
            descuento_cliente = input("Ingrese un codigo de descuento valido o presione enter sino posee ")
            if descuento_cliente == "duoc":
                descuento_compra = 10
                print("---------------------------------")
                print("Descuento Aplicado Correctamente!")
                print("---------------------------------")
            else:
                descuento_compra = 0    
                
            
            validador = False
        case _:
            print("Opcion Invalida! ")
print(f"usted ingreso {contador_opcion1} veces a la opcion 1 ")
print(f"usted ingreso {contador_opcion2} veces a la opcion 2 ")
print(f"usted ingreso {contador_opcion3} veces a la opcion 3 ")
print(f"usted ingreso {contador_opcion4} veces a la opcion 4 ")
print(f"usted ingreso {contador_opcion5} veces a la opcion 5 ")

print(f"usted compro en total {contador_general} productos ")

descuento_aplicable = (contador_dinero * descuento_compra)/100 
total_a_pagar = int((contador_dinero - descuento_aplicable) * 1.19)
print(f"usted gasto en total ${total_a_pagar} IVA incluido")


