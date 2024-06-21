import random
opciones_disponibles = ["Piedra", "Papel", "Tijera", "Papel", "Tijera", "Piedra"]
opcion_usuario = (int(input("Selecciona tu opción para enfrentar a la maquina \n 1. Piedra \n 2. Papel \n 3. Tijera \n")) -1)
seleccion_maquina = opciones_disponibles[random.randint(0, 2)]
print("La maquina ha seleccionado ", seleccion_maquina," y tu has seleccionado ", opciones_disponibles[opcion_usuario])
if seleccion_maquina == opciones_disponibles[opcion_usuario]:
    print("Empate, nadie suma")
elif seleccion_maquina == opciones_disponibles[opcion_usuario + 3]:
    print("La maquina Gana!")
else:
    print("Tú Ganas!")
    
