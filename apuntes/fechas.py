
from datetime import datetime

now = datetime.now()
format = now.strftime('Día :%d, Mes: %m, Año: %Y, Hora: %H, Minutos: %M, Segundos: %S')
print(format)


format2 = now.strftime('%d-%m-%Y')
print(format2)

