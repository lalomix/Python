import random

def adivina_numero_computadora(x):
    
    print ("========================")
    print (" Bienvenido(a) al juego ")
    print ("========================")
    print (f"Selecciona un numero entre 1 y {x} para que la maquina intente adivinar ")
    
    limite_inferior = 1
    limite_superior = x
    
    respuesta = ""
    
    while respuesta != "c":
        if limite_inferior != limite_superior:
            prediccion = random.randint(limite_inferior, limite_superior)
        else:
            prediccion = limite_inferior
            
        respuesta = input(f" mi prediccion es {prediccion}, si es muy alta ingresa A, si es muy baja ingresa B, y si es correcta ingresa C ").lower()
    
        if respuesta == "a":
            limite_superior = prediccion - 1
        elif respuesta == "b":
            limite_inferior = prediccion + 1
            
    print(f" la maquina adivino tu numero, era el  {prediccion}")
    
adivina_numero_computadora(15)