import random

def adivina_el_numero(x):
    
    print ("========================")
    print (" Bienvenido(a) al juego ")
    print ("========================")
    print ("Tu meta es adivinar el numero generado por el juego")
    
    numero_aleatorio = random.randint(1, x)

    predicion = 0
    #vidas = 0
    
    while predicion != numero_aleatorio:
        predicion = int(input(f"Adivina un numero entre el 1 y {x}: "))
        
        if predicion < numero_aleatorio:
            print ("intenta otra vez, elegiste un numero mas bajo que el escogido por la maquina")
        elif predicion > numero_aleatorio:
            print ("intenta otra vez, elegiste un numero mas alto que el escogido por la maquina")
    print (f"Felicitaciones, adivinaste el numero {numero_aleatorio} correctamente")


adivina_el_numero(10)

                