# 4.- Escribe un programa que solicite al usuario ingresar una nota y luego 
# le proporcione una calificación según la siguiente escala (10 puntos):
# 65 o más: A
# 64-50: B
# 49-40: C
# 39-30: D
# Menos de 29: F
calificacion  = ""

nota = int(input("Ingrese la nota para indicar calificación final "))
if nota <= 29:
    calificacion = "F"
elif nota >= 30 and nota <= 39:
    calificacion = "D"
elif nota >= 40 and nota <= 49:
    calificacion = "C"
elif nota >= 50 and nota <= 64:
    calificacion = "B"        
else:
    calificacion = "A"    

print(f"La nota ingresada da como resultado la siguiente calificación: {calificacion}")
