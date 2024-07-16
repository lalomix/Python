from datetime import datetime
##############################FUNCIONES################################
def ganancias_totales(lista):
    ganancias = 0
    for i in lista:
        if(i[1] == "X"):
            ganancias = i[2] + ganancias
    print("Las ganancias totales son $",ganancias)

def comprar_entradas(lista):
    ciclo = True
    while(ciclo):
        entradas = int(input("Ingrese la cantidad de entradas a comprar (1,2,3):"))
        if(entradas < 4 ):
            c = 0
            for asientos in lista:
                if(asientos[1] == "D"):
                    print("[",asientos[0],"]",end="")
                else:
                    print("[ X ]",end="")
                c += 1
                if (c == 10):
                    print("\n")
                    c = 0
            
            asiento_comprar = int(input("Ingrese el asiento que desea comprar:"))
            for i in lista:
                if(i[1] == "X"):
                    print("Asiento ocupado")
                else:    
                    lista[asiento_comprar-1][1] = "X"
                    rut = int(input("Ingrese rut del titular"))
                    i[3] = rut
        else:
            print("Ingrese un valor valido")
        ciclo = False

def mostrar_ubicaciones(diego):
    c = 0
    for asientos in diego:
        #print("El asiento Nº ",asientos[0]," se encuentra: ",asientos[1])
        if(asientos[1] == "D"):
            print("[",asientos[0],"]",end="")
        else:
            print("[ X ]",end="")
        c += 1
        if (c == 10):
            print("\n")
            c = 0


##########################################################################

arena = []
asiento = []
a = 1

for f in range (0,100):
    asiento.append(a)
    asiento.append("D")
    if(a < 21):
        asiento.append(120000)
    elif(a > 20 and a < 51):
        asiento.append(80000)
    else:
        asiento.append(50000)
    asiento.append("RUT")
    arena.append(asiento)
    a += 1
    asiento = []


##################################MAIN###################################
ciclo = True
while(ciclo):
    print("-----------------[MENU]-------------")
    print("1. Comprar entradas")
    print("2. Mostrar ubicaciones disponibles")
    print("3. Ver listado de asistentes")
    print("4. Mostrar ganancias totales")
    print("5. Salir")
    opcion = int(input())
    match opcion:
        case 1:
            comprar_entradas(arena)
        case 2:
            mostrar_ubicaciones(arena)
        case 3:
            print("3")
        case 4:
            ganancias_totales(arena)
        case 5:
            print("Saliendo, Diego Nuñez,",datetime.today())
            ciclo = False
        case _:
            print("Ingrese una opcion valida")
