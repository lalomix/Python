num1 = int(input("ingrese el primer numero "))
num2 = int(input("ingrese el segundo numero "))
try:
    res = num1 / num2
    print(res)
except ZeroDivisionError:
    print("Trataste de dividir entre cero :( ")
except ValueError:
    print("Ingresaste un valor no numerico :( ")    
except TypeError:
    print("Ingresaste un valor no numerico :( ")
except IndexError:
    print("Lo siento, el indice esta fuera de rango")
except KeyError:
  print("¡Lo siento, clave invalida!")
  
#   Tipos de excepciones

# Los principales excepciones definidas en Python son:

#     TypeError : Ocurre cuando se aplica una operación o función a un dato del tipo inapropiado.
#     ZeroDivisionError : Ocurre cuando se itenta dividir por cero.
#     OverflowError : Ocurre cuando un cálculo excede el límite para un tipo de dato numérico.
#     IndexError : Ocurre cuando se intenta acceder a una secuencia con un índice que no existe.
#     KeyError : Ocurre cuando se intenta acceder a un diccionario con una clave que no existe.
#     FileNotFoundError : Ocurre cuando se intenta acceder a un fichero que no existe en la ruta indicada.
#     ImportError : Ocurre cuando falla la importación de un módulo.
