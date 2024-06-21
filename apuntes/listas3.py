

# LISTAS

# nombre_de_variable = [elemento1, elemento2, ...]

frutas = [ "manzana", "naranja", "sandía", "melón"]
edades = [ 18, 35, 45,67, 99 ]
verdades = [ True, False, True, True, False ]
alturas_metro = [ 1.78, 2.34, 1.55, 2.05 ]
palabra = "paralelepipedo"
list1 = ["abc", 34, True, 40, "male"] 

print(frutas[3]) # Imprime Melón, que es el cuarto elemento de la lista
                 # Todas las listas parten de 0
print(len("manzana"))
print(len(edades))
print(palabra[2]) # Los string también se comportan como listas
print(edades[-1]) # Extrae el último elemento
print(frutas[1:3]) # Extrae un subconjunto de la lista desde el elemento 1 al 3 (en este ejemplo) 
## Así como podemos crear un entero a partir de un string
## Podemos crear una lista a partir de una tupla
int("2")
list(("apple", "banana", "cherry"))

# Extrae todo desde el comienzo hasta el elemento anterior al de la cuarta posición
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])
print(thislist[2:])
print(thislist[-4:-1])

if "apple" in thislist: 
    print("Tenemos manzana")
if "maracuya" in thislist: 
    print("Tenemos maracuya")

## Agregar elementos a una lista con el MÉTODO insert()

frutas.insert(len(frutas),"papaya") # agrega al final de la lista
print(frutas)    
frutas.insert(2,"durazno") # agrega en la posición 2 de la lista un elemento
print(frutas) 

## método por defecto para agregar un elemendo al FINAL de la lista

edades.append(44)
print(edades)

## Remover un elemento de la lista
edades.remove(18) # Remueve el elemento de valor 18 de la lista edades
print(edades)
frutas.remove("manzana")
print(frutas)

## Remover mediante la posicion del elemento
frutas.pop(2)
print(frutas) 

## Eliminar una lista de memoria
print(verdades)
del verdades
##print(verdades)

## Limpiar una lista de sus valores
print(list1)
list1.clear()
print(list1)

## Recorrer una lista (DISTINTAS FORMAS DE HACER LO MISMO)

for fruta in frutas:
    print(fruta)
print("______________________________________")
for i in range(len(frutas)):
  print(frutas[i])
print("______________________________________")
for fruta in frutas[1:3]:
    print(fruta)
print("______________________________________")
i = 0
while i < len(frutas):
  print(frutas[i])
  i = i + 1
print("______________________________________")
nombres = ["Eduardo", "Diego", "Constanza", "Catalina", "Javier","Pia"]
nombres_2 = [nombre for nombre in nombres if 4 < len(nombre)<8 ]
nombres_3 = [nombre for nombre in nombres[1:4] if 4 < len(nombre) < 8 ]
print(nombres_2)
print(nombres_3)

frutas_sin_naranja = [ fruta for fruta in frutas if fruta != "naranja"]
print(frutas_sin_naranja)
import time

print( time.time())
numeros_100 = [i for i in range(1,1001)]
print(numeros_100)
print( time.time())

print( time.time())
lista = []
for i in range(1,1001):
   lista.append(i)
print(lista)
print( time.time())