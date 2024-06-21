edad = int(input("ingresa tu edad"))

if edad >= 18 and edad <= 50:
    print("Usted puede beber alcohol")
elif edad <= 8:
    print("usted puede tomar mamadera")
elif edad >=51:
    print("usted puede tomar ensure advance")
else:
    print("usted puede tomar lo que quiera!")