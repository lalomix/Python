# Indicar al usuario que ingrese una palabra
# y asignarlo a la variable user_word.
vocales = ["A", "E", "I", "O", "U"]
new_word = ""
user_word = input("ingresa tu nombre ").upper()

for letter in user_word:
    if letter in vocales:
        new_word = new_word
    else:
        new_word = new_word + letter
print (new_word)


