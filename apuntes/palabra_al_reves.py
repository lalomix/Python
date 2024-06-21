palabra_reversa = ""
palabra = input("ingresa una palabra para invertir: ")

for i in palabra:
    palabra_reversa = i + palabra_reversa
print(palabra_reversa)