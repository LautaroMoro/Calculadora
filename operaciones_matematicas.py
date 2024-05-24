import math as math
def suma(a, b):
    return a + b
def resta(a, b):
    return a - b
def división(a, b):
    if b == 0:
        return a / b
def producto(a, b):
    return a * b
def factorizacion(num):
    if num <= 0:
        print(f"{num} no se puede factorizar debido a que no es posible realizar esa operación con nomeros negativos o que sean iguales a 0")
    else:
        return math.factorial(num)
    