# numero = int(input("ingresa un numero "))

# if numero % 2 == 0:
#     print(f"el numero {numero} es par")
# else:
#     print(f"el numero {numero} es impar")   
    

numeros_pares = 0
numeros_impares = 0

for item in range(1,50):
    if item % 2 == 0:
        numeros_pares += 1
    else:
        numeros_impares += 1
print(f"hay {numeros_pares} numeros pares y {numeros_impares} numeros impares en el segmento que estas ingresando")
        