usuario = {
    "username" : "Eduardo",
    "email" : "eduardo@724.cl",
    "job" : "It Manager",
    "age" : "39",
    "phone": "+56981803585"    
}

print (usuario["phone"])

vista_claves = usuario.keys()
vista_valores = usuario.values()
vista_items = usuario.items()

print(vista_claves)
print(vista_valores)
print(vista_items)


for valor in vista_valores:
    print(f'Valor de mi_diccionario: {valor}')



