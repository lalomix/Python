for i in range(2, 9): #parte en 2 y termina en el indice [9]
    print("El valor de i es", i)
    
print("____________________________________")
    
for i in range(2, 9, 2): # tercer argumento es incremento o salto de x en x
    print("El valor de i es", i)    
    
print("____________________________________")    
    
for i in range (2, 1): # no se ejecuta, segundo valor debe ser mayor a primero
    print("El valor de i es", i)
    
print("____________________________________")       
    

  
objeto = ['colocolo', 'universidaddechile', 'union', 'huachipato', 'Calera']

for i in range(len(objeto)):
    print("mi equipo es ", objeto[i])
    
    
    
for i in range(5):
    print(i)


for i in range(0, 11):
    if i % 2 != 0:
        print(i)