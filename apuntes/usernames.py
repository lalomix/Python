
usernames = []
passwords = []

while True:
    print("¿Qué desea hacer?")
    print("1) Ininiar sesión")
    print("2) Registrar usuario")
    print("3) Eliminar usuario")
    print("4) Salir")
    option = input()

    if option == 4:
        break
    
    username = input("Ingrese nombre de usuario")
    password = input("Ingrese contraseña")

    if option == 1:
        try:
            usernames.index(username)
            passwords.index(password)
            print("Bienvenido: ", username)
        except ValueError:
            print("Usuario no encontrado")
            
    if option == 2:
        usernames.append(username)
        passwords.append(password)
        print("Usuario registrado!")

    if option == 3:
        usernames.remove(username)
        passwords.remove(password)
        print("Usuario eliminado!")


        
