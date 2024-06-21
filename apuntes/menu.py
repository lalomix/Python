total_cuenta = 0
validador = True
descuento = 0
total_productos = 0
cantidad_pr = 0
cantidad_otk = 0
cantidad_pvr = 0
cantidad_aer = 0 

while validador == True:

    print("1. Pikachu Roll                $4500")
    print("2. Otaku Roll                  $5000")
    print("3. Pulpo Venenoso Roll         $5200")
    print("4. Anguila Electrica Roll      $4800")
    print("5. Salir y Pagar               ---->")
    print("\n")
    opcion_usuario = int(input("ingrese la opcion que desea agregar a su pedido: "))

    match opcion_usuario:
        case 1:
            print("\n")
            print("Pikachu Roll agregado al carro exitosamente ")
            total_cuenta = total_cuenta + 4500
            total_productos = total_productos + 1
            cantidad_pr = cantidad_pr + 1 
        case 2:
            print("Otaku Roll agregado al carro exitosamente ")
            total_cuenta = total_cuenta + 5000
            total_productos = total_productos + 1
            cantidad_otk = cantidad_otk + 1
        case 3:
            print("Pulpo Venenoso Roll agregado al carro exitosamente ")
            total_cuenta = total_cuenta + 5200
            total_productos = total_productos + 1
            cantidad_pvr = cantidad_pvr + 1
        case 4:
            print("Anguila Electrica Roll agregado al carro exitosamente ")
            total_cuenta = total_cuenta + 4800
            total_productos = total_productos + 1
            cantidad_aer = cantidad_aer + 1
        case 5:
            print("\n")
            codigo_descuento = input("Ingrese codigo de descuento si posee, sino presione enter ")
            print("\n")
            if codigo_descuento == "soyotaku":
                descuento = 10
            else:
                descuento = 0
            validador = False
        case _:
            print("opcion invalida")

descuento_por_codigo = int(((total_cuenta * descuento)/100))
valor_a_pagar = int(total_cuenta - descuento_por_codigo)

print("**************************")
print(f"TOTAL PRODUCTOS: {total_productos}")
print("**************************")
print(f"Pikachu Roll: {cantidad_pr}")
print(f"Otaku Roll:  {cantidad_otk}")
print(f"Pulpo Venenoso Roll: {cantidad_pvr}")
print(f"Anguila Electrica Roll: {cantidad_aer}")
print("**************************")
print(f"subtotal a pagar: $ {total_cuenta}")
print(f"descuento por codigo: $ {descuento_por_codigo}")
print(f"TOTAL: $ {valor_a_pagar}")
print("\n")