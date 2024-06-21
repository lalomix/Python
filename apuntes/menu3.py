validador = True
subtotal = 0
descuento = 0
contador_arroz  = 0
contador_harina = 0
contador_arroz = 0
contador_general = 0

while validador == True:
    print("=======================")
    print("      BIENVENIDOS      ")
    print("=======================")
    print("1. Arroz ")
    print("2. Harina ")
    print("3. Cerveza ")
    print("4. Vino ")
    print("5. Pagar y Salir ")
    opcion_usuario = int(input("Ingrese la opcion deseada "))
    match opcion_usuario:
        case 1:
            print("Usted ha seleccionado Arroz")
            contador_general = contador_general + 1 
            contador_arroz = contador_arroz + 1
            subtotal = subtotal + 4500
        case 2:
            print("Usted ha seleccionado Harina")
            contador_general = contador_general + 1 
            contador_harina = contador_harina + 1
            subtotal = subtotal + 3500
        case 3:
            print("Usted ha seleccionado Cerveza")
            contador_general = contador_general + 1 
            subtotal = subtotal + 1000
        case 4:
            print("Usted ha seleccionado Vino")
            contador_general = contador_general + 1 
            subtotal = subtotal + 3800
        case 5:
            cupon_descuento = input("ingrese el cupon de descuento si tiene o solo presione enter para omitir descuento ")
            if cupon_descuento == "duoc":
                descuento = 25
            else:
                descuento = 0    
            
            validador = False
        case _:
            print("Opcion invalida! ")

total= subtotal - ((subtotal * descuento)/100)
        
print(f"su cuenta total es de $ {total} y selecciono {contador_arroz} arroz, el total de productos que lleva son {contador_general}")