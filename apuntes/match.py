print("***********************")
print("       Bienvenidos     ")
print("***********************")

gasto = 0
nombre = ""
validador = True
while validador:
    op = int(input("Seleccione una opcion\n \n1.Ingrese su Nombre \n2. Ingrese su Gasto \n3. Mostrar total de gastos \n4. Salir\n"))
    match op:
        case 1:
            nombre=input("Ingrese su nombre\n ")
        case 2:
            gasto += int(input("Ingrese su gasto "))
        case 3:
            print(f"El total de gastos del usuario: {nombre} es de ${gasto} ")
        case 4:
            validador = False
        case _:
            print("la opcion ingresa es erronea")

#git clone https://github.com/diegoroblesrivera/FP3