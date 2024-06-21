matriz = []
matriz2 = []
for i in range(3):
    for j in range(4):
        matriz2.append(int(input("Ingrese un numero: ")))
    matriz.append(matriz2)
    matriz2 = []

n=0
for i in range(3):
    print(matriz[n])
    n +=1
    
import random
cubo = ["amarillo", "rojo", "naranjo", "verde", "blanco"]
new_cubo = []
ama =0
rojo = 0
nara=0
verd=0
blanc=0

for i in range(3):
    for j in range(3):
        for k in range(3):
            new_cubo.append(random.choice(cubo))
            if random.choice(cubo) == "amarillo":
                ama+=1
            elif random.choice(cubo) == "rojo":
                rojo+=1
            elif random.choice(cubo) == "naranjo":
                nara+=1
            elif random.choice(cubo) == "verde":
                verd+=1
            else:
                blanc+=1
print(f"la cantidad de fichas amarillas son: {ama}")
print(f"la cantidad de fichas rojas son: {rojo}")
print(f"la cantidad de fichas naranjas son: {nara}")
print(f"la cantidad de fichas verde son: {verd}")
print(f"la cantidad de fichas blancas son: {blanc}")