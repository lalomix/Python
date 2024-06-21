# 3.- Escribe un programa que solicite al usuario ingresar un número entero positivo y luego imprima la cantidad de números 
# pares e impares dentro del rango de 1 a ese número (10 puntos).

num_par = 0
num_impar = 0

numero_usuario = int(input("Ingrese un numero entero positivo "))
for item in range(1,numero_usuario+1):
    if item % 2 == 0:
        num_par += 1
    else:
        num_impar +=1
print(f"Entre el 1 y el {numero_usuario}, la cantidad de numeros pares es: {num_par}, y la cantidad de impares es: {num_impar} ")
