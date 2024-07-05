# recorrer diccionarios 

pol_esp_dictionary = {
    "zamek": "castillo",
    "woda": "agua",
    "gleba": "tierra"
    }

for item in pol_esp_dictionary:
    print(item)

for key, value in pol_esp_dictionary.items():
    print(key, ":", value) 

#unir diccionarios    
d1 = {'Adam Smith': 'A', 'Judy Paxton': 'B+'}
d2 = {'Mary Louis': 'A', 'Patrick White': 'C'}
d3 = {}

for item in (d1, d2):
    d3.update(item)

print(d3)

colors = {
    "blanco": (255, 255, 255),
    "gris": (128, 128, 128),
    "rojo": (255, 0, 0),
    "verde": (0, 128, 0)
    }

for col, rgb in colors.items():
    print(col, ":", rgb) 