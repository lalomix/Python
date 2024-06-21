try:
	# Codigo a ejecutar
	# Pero podria haber errores en este bloque
    
except <tipo de error>:
	# Haz esto para manejar la excepcion
	# El bloque except se ejecutara si el bloque try lanza un error
    
else:
	# Esto se ejecutara si el bloque try se ejecuta sin errores
   
finally:
    
    
    # EL bloque try es el bloque con las sentencias que quieres ejecutar. Sin embargo, podrían llegar a haber errores de ejecución  y el bloque se dejará de ejecutarse.
    # El bloque except se ejecutará cuando el bloque try falle debido a un error. Este bloque contiene sentencias que generalmente nos dan un contexto de lo que salió mal en el bloque try.
    # Siempre deberías de mencionar el tipo de error que se espera, como una excepción dentro del bloque except dentro de <tipo de error> como lo muestra el ejemplo anterior.
    # Podrías usar except sin especificar el <tipo de error>. Pero no es una práctica recomendable, ya que no estarás al tanto de los tipos de errores que puedan ocurrir.
    
# Tipos de excepciones

# Los principales excepciones definidas en Python son:

#     TypeError : Ocurre cuando se aplica una operación o función a un dato del tipo inapropiado.
#     ZeroDivisionError : Ocurre cuando se itenta dividir por cero.
#     OverflowError : Ocurre cuando un cálculo excede el límite para un tipo de dato numérico.
#     IndexError : Ocurre cuando se intenta acceder a una secuencia con un índice que no existe.
#     KeyError : Ocurre cuando se intenta acceder a un diccionario con una clave que no existe.
#     FileNotFoundError : Ocurre cuando se intenta acceder a un fichero que no existe en la ruta indicada.
#     ImportError : Ocurre cuando falla la importación de un módulo.
