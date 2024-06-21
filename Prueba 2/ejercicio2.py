# 2.- Escribe un programa en Python que solicite al usuario ingresar su edad. 
# El programa validará si la edad ingresada se encuentra dentro del rango permitido entre 10 y 80 años. 
# Si la edad está fuera de este rango, mostrará un mensaje de error indicando que el número ingresado está fuera del rango permitido. 
# Además, el programa manejará excepciones para evitar errores en caso de que el usuario ingrese un tipo de dato diferente a un número entero,
# mostrando un mensaje de error adecuado en caso de que esto ocurra. El programa continuará solicitando la edad hasta que se ingrese un valor 
# válido dentro del rango especificado (15 puntos). 

validador = True
while validador:
    try:
        edad_usuario = int(input("Ingrese su edad "))
        if edad_usuario >= 10 and edad_usuario <= 80:
            print("Edad dentro del rango! ")
            validador = False
        else:
            print("Edad fuera del rango, intentalo nuevamente! ")
    except ValueError:
        print("Ha ingresado un dato no valido, favor reintente")
