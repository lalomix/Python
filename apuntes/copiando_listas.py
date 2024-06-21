# Copiando la lista completa.
list_1 = [1]
list_2 = list_1[:]
list_1[0] = 2
print(list_2)
print(list_1)
# Copiando parte de la lista.
my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:3]
print(new_list)


my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:-1] # negativo recorre de atras para adelante
print(new_list)



my_list = [10, 8, 6, 4, 2]
new_list = my_list[:3]#es posible omitir incio y comenzar del indice 0
print(new_list)
 
# copiando toda la lista
my_list = [10, 8, 6, 4, 2]
new_list = my_list[:]
print(new_list)
 
