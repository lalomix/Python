import random

number1 = random.randint(1, 50)
number2 = random.randint(1, 50)
number3 = random.randint(1, 50)

largest_number = max(number1, number2, number3 )


print(f"\n Entre los numeros {number1}, {number2}, y {number3}  el numero mayor es {largest_number} \n" )
