#EJERCICIO 1

# cantidad_nombres = 3
# nombre_mayor = ""
# for i in range(cantidad_nombres):
#     nombre = input(f"Ingrese el nombre N°{i+1} ")
#     if len(nombre) > len(nombre_mayor):
#         nombre_mayor = nombre 
# print(f"el nombre mayor es {nombre_mayor}")


# EJERCICIO 2

# nombres = ["David", "Eduardo", "Diego"]
# apellidos = ["Joo", "Vargas", "Nuñez"]
# for i in range(len(nombres)):
#     print (nombres[i], apellidos[i])

#EJERCICIO 3

# names = []
# answer = "si"
# while answer != "no":
#     names.append(input("Ingrese un nombre "))
#     answer = input("Desea agregar otro nombre? (si/no) ").lower()
# names.remove(sorted(names, key=len)[0])
# print (names)

###########################################################################################

# Ejercicio 4

usuarios = ["eduardo","ruben", "diego"]
contrasenas = ["123456","contraseña","colocolo"]

while True:
    print("===============================")
    print("         Bienvenidos           ")
    print("===============================")
    print("\n")
    print("1. Iniciar Sesion ")
    print("2. Registrar Usuario")
    print("3. Eliminar Usuario")
    print("4. Salir ")
    opcion = int(input("Ingrese la opción que desea "))
    match opcion:
        case 1:
            nombre_usuario = input("ingrese nombre de usuario ")
            if nombre_usuario in list(usuarios):
                contrasena_usuario = input("ingrese contraseña ")
                if 
                
            else:
                print("Usuario no encontrado! ")
        case 2:
            nombre_usuario = input("ingrese nombre de usuario ")
            if nombre_usuario in list(usuarios):
                contrasena_usuario = input("ingrese contraseña ")
            else:
                print("Usuario no encontrado! ")
        case 3:
            print("opcion3 ")
        case 4:
            break
            

