import operaciones_matematicas as operadores
def mostrar_menu(a, b):
    print("Calculadora")
    print(f"1. Ingrese el primer numero({a})")
    print(f"2. Ingrese el 2do numero({b})")
    print("3. Realizar operaciones")
    print("4. Mostrar los resultados")
    print("5. Salir")

def menu(a, b):
    a = 0
    b = 0
    suma = 0
    resta = 0
    producto = 0
    factorizacion_a = 0
    factorizacion_b = 0
    division = 0
    while True:
        mostrar_menu(a, b)
        funcion = input("Seleccione una función de la calculadora para usar: ")
        if funcion == 1:
            a = input("Ingrese el primer numero(a)")
            a = float(a)
        elif funcion == "2":
            b = input("Ingrese el primer numero(b)")
            b = float(b)
        elif funcion == "3":
            suma = operadores.suma(a, b)
            resta = operadores.resta(a, b)
            producto = operadores.producto(a, b)
            division = operadores.division(a, b)
            factorizacion_a = operadores.factorizacion(a)
            factorizacion_b = operadores.factorizacion(b)
        elif funcion == "4":
            print(f"el resultado de la suma es: {suma}")
            print(f"el resultado de la resta es: {resta}")
            print(f"El resultado del producto es: {producto}")
            print(f"El resultado de la división es: {division}")
            print(f"El resultado de la factorizacion del primer numero ingresado es: {factorizacion_a}")
            print(f"El resultado de la factorización del segundo numero ingresado es: {factorizacion_b}")
        elif funcion == "5":
            break

            



