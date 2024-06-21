#########################################################################################################################
#
# Programa para enctiptar contraseña: 
### La contraseña será sólo de letras mayúsculas
### La encriptación consiste en convertir cada letra del abecesario por la letra correspondiente al abecesario invertido
### Ejemplo: La A es la Z, la B es la Y, la C es la X y viceversa. 
### Ejemplo: Si la contraseña es APBT la encriptación es ZKYG
#
#########################################################################################################################



# Definición de constantes a usar en todo el programa
# interface = arreglo de números a sumar o restar para convertir el valor ASCII del caracter a encryptar o desencryptar
# abc_1 = arreglo con los valores ascii de la A a la N
# abc_2 = arreglo con los valores ascii de la O a la Z

interface = [25,23,21,19,17,15,13,11,9,7,5,3,1]
abc_1 = [65,66,67,68,69,70,71,72,73,74,75,76,77]
abc_2 = [90,89,88,87,86,85,84,83,82,81,80,79,78]

def encrypt(password):
    password_encrypted = ""
    ascii = 0
    for letter in password: # Esto se lee como: "Para cada letra en la contraseña, hacer..."
        ascii = ord(letter) # Rescato el valor ascii de la letra con la función ord()
        if(ascii in abc_1): # Si el valor está en el primer arreglo
            # Se le suma el valor del caracter invertido a la contraseña encriptada
            # Se obtiene la letra correspondiente sumando el numero que tiene la misma posicion (indice) en el arreglo de interface
            # Ejemplo: La letra A ocupa el índice 0 en el arregle abc_1, 
            #          por lo tanto se le debe sumar el valor en el índice 0 del arreglo interface 
            password_encrypted = password_encrypted + chr(ascii + interface[abc_1.index(ascii)])
        if(ascii in abc_2):
            # Si el valor está en el segundo arreglo
            # Se obtiene la letra correspondiente restando el numero que tiene la misma posicion (indice) en el arreglo de interface
            # Ejemplo: Si la letra es la Z (ascii = 90) debo restarle 25 para que se convierta en A (ascii = 65)
            password_encrypted = password_encrypted + chr(ascii - interface[abc_2.index(ascii)])


    return password_encrypted

password = input("Ingrese su contraseña a encriptar: ")
print(encrypt(password))
